import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(3,GPIO.IN,pull_up_down = GPIO.PUD_UP)
global x
x=0
def increment():
    if x<3:
        x = x+1
        Pattern()
    else:
        x = 0
        print(x)
        sleep(0.2)
def Pattern():
    while x == 0:
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        if GPIO.input(3) == GPIO.LOW:
            increment()
    while x == 1:
        GPIO.output(8, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(8, GPIO.LOW)
        sleep(0.2)
        GPIO.output(10, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(10, GPIO.LOW)
        sleep(0.2)
        GPIO.output(12, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(12, GPIO.LOW)
        sleep(0.2)
        GPIO.output(16, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(16, GPIO.LOW)
        sleep(0.2)
        if GPIO.input(3) == GPIO.LOW:
            increment()
    while x==2:
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.HIGH)
        sleep(0.2)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(12,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        sleep(0.2)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.HIGH)
        sleep(0.2)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(12,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        sleep(0.2)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        sleep(0.4)
        if GPIO.input(3) == GPIO.LOW:
            increment()
    while x==3:
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(12,GPIO.HIGH)
        sleep(0.2)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        sleep(0.2)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(12,GPIO.HIGH)
        sleep(0.2)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        sleep(0.2)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        if GPIO.input(3) == GPIO.LOW:
            increment()
while True:
        if GPIO.input(3) == GPIO.LOW:
            if x<3:
                x = x+1
                Pattern()
            else:
                x = 0
        print(x)
        sleep(0.2)
    


        
    
    

