#!/usr/bin/python

from boto import sqs
import json
import time

conn = sqs.connect_to_region("us-east-1",
  aws_access_key_id="AKIAIAZFZFPNAV3QPD2Q",
  aws_secret_access_key="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")

queue = conn.get_queue("FlyerDR-scraper-requests")

obj = {'timestamp': time.time(), 'message_type': 'rewards_balance_refresh',
       "params": {"rewards_program_account_revision_id": 2 }}

def put_json(o):
  m = sqs.message.Message()
  m.set_body(json.dumps(o))
  queue.write(m)

put_json(obj)
