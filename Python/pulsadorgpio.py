import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
GPIO.setup(7, GPIO.OUT)

while True:
   if GPIO.input(3):
      GPIO.output(7, False)
   else:
      GPIO.output(7, True)