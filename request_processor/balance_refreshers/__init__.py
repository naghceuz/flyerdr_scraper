import subprocess
import os, inspect

all_refreshers = ["aa", "delta", "jet","united","asia"]

def run_refresher_script(name, arg1, arg2):
  if name not in all_refreshers:
    raise ValueError("Invalid airline name")
  path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
  exe = os.path.join(path, name +".py")
  output = subprocess.check_output(["xvfb-run", "python", exe, arg1, arg2])
  return [(int(output), None)]

