"""
Nombre: puerto8bits.py
Objetivo:encender led con raspberry.
Autor: Andrés Eduardo Mora Alonso
Fecha: //
"""

import RPi.GPIO as GPIO 
from time import sleep
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)

def reset():
    GPIO.output(3, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)

def ceroEfe():
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    sleep(1)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    sleep(1)
    
#Corrimientos de izquiera a derecha.

def main():
    while True: # Run forever
        ceroEfe()

if __name__=='__main__':
    main()