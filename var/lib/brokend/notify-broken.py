#!/usr/bin/env python3

from systemd import journal

journal.send('Emiting failure notification.')
with open('/tmp/emmit-notification', 'w') as ostream:
  ostream.write('notify failure')



