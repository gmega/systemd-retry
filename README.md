# Rate-limited Service Restarts with Failure Notification on systemd

This repo contains a simple example of a [systemd](https://www.freedesktop.org/wiki/Software/systemd/) policy which:

  1. attempts to restart a service at most `X` times over a time interval of `Y` seconds, and;
  2. in case it is unable to, triggers a notification script.

This is useful for rendering fault-tolerant services which die every once in a while due to transient faults, while still preserving the ability to detect cases in which the fault is not actually transient.

**NOTE:** This policy requires systemd 239 or later. Earlier versions of systemd [had issues](https://github.com/systemd/systemd/issues/8398) which render such policies difficult, if not impossible, to represent.