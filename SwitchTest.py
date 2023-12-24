import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(3,GPIO.IN,pull_up_down = GPIO.PUD_UP)
while True :
    if(GPIO.input(3)):
        GPIO.output(8,GPIO.LOW)
    else:
        GPIO.output(8,GPIO.HIGH)