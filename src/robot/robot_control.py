import RPi.GPIO as io
import time
import os
import pygame
import sys
from pygame.locals import *

os.environ['SDL_VIDEODRIVER'] = 'dummy' #fake display

pygame.display.set_mode((1,1))          #fake display

clock = pygame.time.Clock()

crashed = False

gear = 2
pServo1 = 4
pServo2 = 9

channels = (11,17,22,27,26,9,10)
motor_pins = (11,17,22,27)

def setup_joystick():
 global joystick
 pygame.init()
 pygame.joystick.init()
 joystick = pygame.joystick.Joystick(0)
 joystick.init()

# joystick_count = pygame.joystick.get_count()
# numaxes = joystick.get_numaxes()
# numbuttons = joystick.get_numbuttons()

def setup_channels(channels):
 io.setmode(io.BCM)
 io.setwarnings(False)
 io.setup(channels,io.OUT)

def setup_pwm():
 global pwm_motor1
 global pwm_motor2
 global pwm_servo
 pwm_motor1 = io.PWM(9,100)         #PWM motor1
 pwm_motor2 = io.PWM(10,100)       #PWM motor2
 pwm_servo = io.PWM(26,50)  #PWM servo motor
 pwm_motor1.start(0)          #PWM motor1
 pwm_motor2.start(0)         #PWM motor2
 pwm_servo.start(0)   #PWM servo motor

def forward():
 io.output(11,0)
 io.output(17,1)
 io.output(22,1)
 io.output(27,0)

def backward():
 io.output(11,1)
 io.output(17,0)
 io.output(22,0)
 io.output(27,1)

def right():
 io.output(11,1)
 io.output(17,0)
 io.output(22,1)
 io.output(27,0)

def left():
 io.output(11,0)
 io.output(17,1)
 io.output(22,0)
 io.output(27,1)

def stop():
 io.output(11,0)
 io.output(17,0)
 io.output(22,0)
 io.output(27,0)

def forwardLeft():
 global pwm_motor1
 pwm_motor1.ChangeDutyCycle(20)
 io.output(11,0)
 io.output(17,1)
 io.output(22,1)
 io.output(27,0)

def forwardRight():
 global pwm_motor2
 pwm_motor2.ChangeDutyCycle(20)
 io.output(11,0)
 io.output(17,1)
 io.output(22,1)
 io.output(27,0)

def pwmGearZero():
 global pwm_motor1
 global pwm_motor2
 pwm_motor1.ChangeDutyCycle(0)
 pwm_motor2.ChangeDutyCycle(0)

def pwmGearOne():
 global pwm_motor1
 global pwm_motor2
 pwm_motor1.ChangeDutyCycle(30)
 pwm_motor2.ChangeDutyCycle(30)

def pwmGearTwo():
 global pwm_motor1
 global pwm_motor2
 pwm_motor1.ChangeDutyCycle(50)
 pwm_motor2.ChangeDutyCycle(50)

def pwmGearThree():
 global pwm_motor1
 global pwm_motor2
 pwm_motor1.ChangeDutyCycle(75)
 pwm_motor2.ChangeDutyCycle(75)

def pwmGearFour():
 global pwm_motor1
 global pwm_motor2
 pwm_motor1.ChangeDutyCycle(100)
 pwm_motor2.ChangeDutyCycle(100)

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
 global joystick
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

# if joystick.get_axis(1) < 0:
#  left()
#  print("left")
# if joystick.get_axis(1) < 0 and joystick.get_button(9) == 1:
#  forwardLeft()

# if joystick.get_axis(1) > 0.1:
#  right()
#  print("right")
# if joystick.get_axis(1) > 0.1 and joystick.get_button(9) == 1:
#  forwardRight()
    
 if joystick.get_button(9) == 0 and joystick.get_button(8) == 0 and joystick.get_button(5) == 0 and joystick.get_button(7) == 0:
  stop()
# if joystick.get_axis > -0.1 and joystick.get_axis(1) < 0.1:
#  stop()

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

def eventControl(e):
 global joystick
 if e.type == pygame.QUIT:
  crashed = True
 if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
  crashed = True

 if e.type == pygame.JOYBUTTONDOWN:
  if joystick.get_button(9) == 1:
   print("forward")
  if joystick.get_button(8) == 1:
   print("backward")
  if joystick.get_button(7) == 1:
   print("left")
  if joystick.get_button(7) == 1 and joystick.get_button(9) == 1:
   print("forwardleft")
  if joystick.get_button(5) == 1:
   print("right")
  if joystick.get_button(5) == 1 and joystick.get_button(9) == 1:
   print("forwardright")
  if joystick.get_axis(1) <= -0.5:
   print("left")
  if joystick.get_axis(1) <= -0.5 and joystick.get_button(9) == 1:
   print("forwardLeft")
  if joystick.get_axis(1) >= 0.5:
   print("right")
  if joystick.get_axis(1) >= 0.5 and joystick.get_button(9) == 1:
   print("forwardRight")

def GearControl():
 global joystick
 global switchCounter
 if joystick.get_button(10) == 1 and switchCounter > delay:
  SwitchGearDown()
  switchCounter = 0
    
 if joystick.get_button(11) == 1 and switchCounter > delay:
  SwitchGearUp() 
  switchCounter = 0

def ServoControl():
 global joystick
 global pwm_servo
 if joystick.get_button(13) == 0 and joystick.get_button(15) == 0:
  pwm_servo.ChangeDutyCycle(0)

 if joystick.get_axis(2) >= 0.5:
  pwm_servo.ChangeDutyCycle(pServo2)
 # print("servo rotating right")
 
 if joystick.get_axis(2) <= -0.5:
  pwm_servo.ChangeDutyCycle(pServo1)
 # print("servo rotating left")


def main():
 global joystick
 global switchCounter
 try:
  setup_joystick()
  setup_channels(channels)
  setup_pwm()
  while not crashed:
   timer = time.time()
   events = pygame.event.get()
   for e in events:
    eventControl(e)      
   
   Gear()   
   JoystickControl()   
   GearControl() 
   ServoControl()   

#   print(joystick.get_axis(1))
#   print(joystick.get_axis(2))
   switchCounter+=1
 
   pygame.display.update()
   clock.tick(60)

 except KeyboardInterrupt:
  pygame.quit()
  io.cleanup()
  pwm_motor1.stop()
  pwm_motor2.stop()
  pwm_servo.stop()
  quit()
 
if __name__ == "__main__":
 main()
