#!/usr/bin/env python3

from systemd import journal
import time
import os

MAX_FAILURES = 5
TIME_TO_FAILURE = 1
COUNTER_FILE = '/tmp/counter'

try:
  count = int(open(COUNTER_FILE, 'r').read())
except FileNotFoundError:
  count = 0

journal.send(f'Broken service is starting: {count}.')

with open(COUNTER_FILE, 'w') as ostream:
  ostream.write(str(count + 1))

time.sleep(TIME_TO_FAILURE)

if count < MAX_FAILURES:
  raise Exception('Ooooooh I\'ve failed!')

os.remove('/tmp/counter')

journal.send('Broken service is online.')

time.sleep(100000)