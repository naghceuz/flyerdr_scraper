#!/usr/bin/python

import json
import traceback
import time
from boto import sqs
import MySQLdb

import config
import balance_refreshers

conn = sqs.connect_to_region(config.QUEUE_REGION,
  aws_access_key_id=config.AWS_ACCESS_KEY_ID,
  aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY)

queue = conn.get_queue(config.QUEUE_NAME)

AWESOME_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

def get_json_or_none():
  rs = queue.get_messages(1)
  if len(rs) == 0:
    return None, None

  try:
    msg = json.loads(rs[0].get_body())
  except: # Invalid JSON, hopefully it ends in the deadletter queue
    return None, None

  return rs[0], msg

def log_message(o):
  log_line = time.strftime("["+AWESOME_TIME_FORMAT+"]")
  log_line += " " + o["message_type"] + " from "
  log_line += time.strftime(AWESOME_TIME_FORMAT, time.gmtime(o["timestamp"]))
  print log_line

def get_mysql_connection():
  return MySQLdb.connect(host=config.MYSQL_HOST,
                      user=config.MYSQL_USER,
                      passwd=config.MYSQL_PASS,
                      db=config.MYSQL_SCHEMA)

# Returns list of tuples
# (Balance, Expiration)
# expiration is either YYYY-MM-DD string or None
def get_balance_parts(shortname, cred1, cred2):
  return balance_refreshers.run_refresher_script(shortname, cred1, cred2)

def process_rewards_balance_refresh(revision_id):
  mc = get_mysql_connection()
  c = mc.cursor()
  try:
      c.execute("""
SELECT rp.shortname, rpa.cred1, rpa.cred2
FROM pointstracker_rewardsprogramaccountrevision rpar
LEFT JOIN pointstracker_rewardsprogramaccount rpa ON rpa.id = rpar.account_id
LEFT JOIN pointstracker_rewardsprogram rp ON rp.id=rpa.rewards_program_id
WHERE rpar.id=%s AND pending=1""", (revision_id,))
      shortname, cred1, cred2 = c.fetchone()

      balance_parts = get_balance_parts(shortname, cred1, cred2)

      c.executemany("""INSERT INTO pointstracker_rewardsprogramaccountrevisionentry
        (amount, expiration_date, revision_id) VALUES (%s, %s, %s)""",
         [(x, y, revision_id) for (x,y) in balance_parts])

      c.execute("""UPDATE pointstracker_rewardsprogramaccountrevision
         SET pending = 0 WHERE id=%s""", (revision_id,))
  except Exception as e:
    raise e
  else:
    mc.commit()
  finally:
    mc.close()

def process_message(o):
  log_message(o)

  if o["message_type"] != "rewards_balance_refresh":
    raise ValueError("Invalid message_type")

  process_rewards_balance_refresh(o["params"]["rewards_program_account_revision_id"])

  print "Done processing message."

while True:
  msg, obj = get_json_or_none()
  if obj is None: continue

  try:
    process_message(obj)
  except Exception as e:
    print "Exception while processing message!"
    traceback.print_exc()
    queue.delete_message(msg)
  else:
    queue.delete_message(msg)
