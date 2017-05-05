import RPi.GPIO as GPIO
import time

gearOne = 35
gearTwo = 50
gearThree = 75
gearFour = 100

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT) #motor 2
GPIO.setup(17,GPIO.OUT) #motor 2
GPIO.setup(22,GPIO.OUT) #motor 1
GPIO.setup(27,GPIO.OUT) #motor 1

GPIO.setup(9,GPIO.OUT)  #PWM 1
GPIO.setup(10,GPIO.OUT) #PWM 2

p = GPIO.PWM(9,100)
p2 = GPIO.PWM(10,100)

def PWMenable():
 p.start(0)   #PWM
 p2.start(0) #PWM

def forward():
 GPIO.output(18,0)
 GPIO.output(17,1)
 GPIO.output(22,1)
 GPIO.output(27,0)

def backward():
 GPIO.output(18,1)
 GPIO.output(17,0)
 GPIO.output(22,0)
 GPIO.output(27,1)

def left():
 GPIO.output(18,1)
 GPIO.output(17,0)
 GPIO.output(22,1)
 GPIO.output(27,0)

def right():
 GPIO.output(18,0)
 GPIO.output(17,1)
 GPIO.output(22,0)
 GPIO.output(27,1)

def stop():
 GPIO.output(18,0)
 GPIO.output(17,0)
 GPIO.output(22,0)
 GPIO.output(27,0)

def pwmZero():
 p.ChangeDutyCycle(0)
 p2.ChangeDutyCycle(0)

def pwmGearOne():
 p.ChangeDutyCycle(gearOne)
 p2.ChangeDutyCycle(gearOne)

def pwmGearTwo():
 p.ChangeDutyCycle(gearTwo)
 p2.ChangeDutyCycle(gearTwo)

def pwmGearThree():
 p.ChangeDutyCycle(gearThree)
 p2.ChangeDutyCycle(gearThree)

def pwmGearFour():
 p.ChangeDutyCycle(100)
 p2.ChangeDutyCycle(100)

try:
 while True:
  PWMenable()
  pwmGearFour()
  backward()
  time.sleep(2)
  stop()
  time.sleep(1)
except KeyboardInterrupt:
 GPIO.cleanup()
 p.stop()
 p2.stop()
 
