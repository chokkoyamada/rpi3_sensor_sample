#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time,os
import RPi.GPIO as GPIO
import send_push

INTAVAL = 3
SLEEPTIME = 5
SENSOR_PIN = 18

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(SENSOR_PIN, GPIO.IN)
GPIO.setup(22, GPIO.OUT)

st = time.time()-INTAVAL

try:
  for i in range(30):
    print GPIO.input(SENSOR_PIN)
    if(GPIO.input(SENSOR_PIN) == GPIO.HIGH) and (st + INTAVAL < time.time()):
      st = time.time()
      print("人を感知しました")
      os.system('sh post.sh Detected_something! ')
      send_push.test_push()
      GPIO.output(22, True)
    else:
      GPIO.output(22, False)
    time.sleep(SLEEPTIME)

except KeyboardInterrupt:
  print "KeyboardInterrupt"

except:
  print "Other error or exception occurred!"

finally:
  GPIO.cleanup()
