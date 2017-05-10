import RPi.GPIO as GPIO
import time, os

os.environ['SDL_VIDEODRIVER'] = 'dummy' #fake display
import pygame, sys
pygame.display.set_mode((1,1))          #fake display
from pygame.locals import *
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

joystick_count = pygame.joystick.get_count()
numaxes = joystick.get_numaxes()
numbuttons = joystick.get_numbuttons()

clock = pygame.time.Clock()

crashed = False

gear = 1
pServo1 = 7.25
pServo2 = 7.6

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(11,GPIO.OUT) #motor 2
GPIO.setup(17,GPIO.OUT) #motor 2
GPIO.setup(22,GPIO.OUT) #motor 1
GPIO.setup(27,GPIO.OUT) #motor 1
GPIO.setup(26,GPIO.OUT) #servo motor
GPIO.setup(9,GPIO.OUT)  #PWM 1
GPIO.setup(10,GPIO.OUT) #PWM 2

p = GPIO.PWM(9,100)         #PWM motor1
p2 = GPIO.PWM(10,100)       #PWM motor2
pwmServo = GPIO.PWM(26,50)  #PWM servo motor
p.start(0)          #PWM motor1
p2.start(0)         #PWM motor2
pwmServo.start(0)   #PWM servo motor

def forward():
 print("forward")
 GPIO.output(11,0)
 GPIO.output(17,1)
 GPIO.output(22,1)
 GPIO.output(27,0)

def backward():
 print("backward")
 GPIO.output(11,1)
 GPIO.output(17,0)
 GPIO.output(22,0)
 GPIO.output(27,1)

def right():
 print("right")
 GPIO.output(11,1)
 GPIO.output(17,0)
 GPIO.output(22,1)
 GPIO.output(27,0)

def left():
 print("left")
 GPIO.output(11,0)
 GPIO.output(17,1)
 GPIO.output(22,0)
 GPIO.output(27,1)

def stop():
 GPIO.output(11,0)
 GPIO.output(17,0)
 GPIO.output(22,0)
 GPIO.output(27,0)

def forwardLeft():
 print("forwardleft")
 p.ChangeDutyCycle(10)
 GPIO.output(11,0)
 GPIO.output(17,1)
 GPIO.output(22,1)
 GPIO.output(27,0)

def forwardRight():
 print("forwardright")
 p2.ChangeDutyCycle(10)
 GPIO.output(11,0)
 GPIO.output(17,1)
 GPIO.output(22,1)
 GPIO.output(27,0)

def pwmGearZero():
 p.ChangeDutyCycle(0)
 p2.ChangeDutyCycle(0)

def pwmGearOne():
 p.ChangeDutyCycle(20)
 p2.ChangeDutyCycle(20)

def pwmGearTwo():
 p.ChangeDutyCycle(40)
 p2.ChangeDutyCycle(40)

def pwmGearThree():
 p.ChangeDutyCycle(60)
 p2.ChangeDutyCycle(60)

def pwmGearFour():
 p.ChangeDutyCycle(100)
 p2.ChangeDutyCycle(100)

def Gear():
 global gear
 if gear == 1:
  pwmGearOne()
 elif gear == 2:
  pwmGearTwo()
 elif gear == 3:
  pwmGearThree()
 elif gear == 4:
  pwmGearFour()

def JoystickControl():
 if joystick.get_button(9) == 1:
  forward()

 if joystick.get_button(8) == 1:
  backward()

 if joystick.get_button(7) == 1:
  left()

 if joystick.get_button(7) == 1 and joystick.get_button(9) == 1:
  forwardLeft()
  
 if joystick.get_button(5) == 1:
  right()
  
 if joystick.get_button(5) == 1 and joystick.get_button(9) == 1:
  forwardRight()
    
 if joystick.get_button(9) == 0 and joystick.get_button(8) == 0 and joystick.get_button(5) == 0 and joystick.get_button(7) == 0:
  stop()

def SwitchGearDown():
 global gear 
 if gear == 1:
  gear = 1
  print("already lowest gear")
 elif gear == 2:
  gear = 1
  print("gear 1")
 elif gear == 3:
  gear = 2
  print("gear 2")
 elif gear == 4:
  gear = 3
  print("gear 3")

def SwitchGearUp():
 global gear
 if gear == 1:
  gear = 2
  print("gear 2")
 elif gear == 2:
  gear = 3
  print("gear 3")
 elif gear == 3:
  gear = 4
  print("gear 4")
 elif gear == 4:
  gear = 4
  print("already highest gear")

delay = 30
switchCounter = 0

def eQuit(e):
 if e.type == pygame.QUIT:
  crashed = True
 if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
  crashed = True

def GearControl():
 global switchCounter
 if joystick.get_button(10) == 1 and switchCounter > delay:
  SwitchGearDown()
  switchCounter = 0
    
 if joystick.get_button(11) == 1 and switchCounter > delay:
  SwitchGearUp() 
  switchCounter = 0

def ServoControl():
 if joystick.get_button(13) == 0 and joystick.get_button(15) == 0:
  pwmServo.ChangeDutyCycle(0)

 if joystick.get_axis(2) >= 0.5:
  pwmServo.ChangeDutyCycle(pServo2)
  print("servo rotating right")
 if joystick.get_axis(2) <= -0.5:
  pwmServo.ChangeDutyCycle(pServo1)
  print("servo rotating left")


def main():
 global switchCounter
 try:
  while not crashed:
   timer = time.time()
   events = pygame.event.get()
   for e in events:
    eQuit(e)      
    Gear()   
    JoystickControl()   
    GearControl() 
    ServoControl()   
#    if joystick.get_button(13) == 0 and joystick.get_button(15) == 0:
#     pwmServo.ChangeDutyCycle(0)

#    if joystick.get_axis(2) >= 0.5:
#     pwmServo.ChangeDutyCycle(pServo2)
#    if joystick.get_axis(2) <= -0.5:
#     pwmServo.ChangeDutyCycle(pServo1)

   #print(joystick.get_axis(1))
   #print(joystick.get_axis(2))
   switchCounter+=1
 
   pygame.display.update()
   clock.tick(60)

 except KeyboardInterrupt:
  pygame.quit()
  GPIO.cleanup()
  p.stop()
  p2.stop()
  quit()
 
if __name__ == "__main__":
 main()
