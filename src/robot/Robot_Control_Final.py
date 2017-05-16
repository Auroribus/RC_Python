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
pwm_servo_left_low = 7.3
pwm_servo_left_high = 4
pwm_servo_right_low = 7.5
pwm_servo_right_high = 9

channels = (11,17,22,27,26,9,10)

delay_gear_switch = 20
counter_gear_switch = 0
delay_print = 50
counter_print = 0

D_pad_left = 7
D_pad_right = 5
D_pad_up = 4
D_pad_down = 6
Square = 15
Triangle = 12
Circle = 13
Cross = 14
L1 = 10
L2 = 8
R1 = 11
R2 = 9
Select = 0
Start = 3
left_stick_LeftRight = 0
left_stick_UpDown = 1
right_stick_LeftRight = 2
right_stick_UpDown = 3

def setup_joystick():
 global joystick
 pygame.init()
 pygame.joystick.init()
 joystick = pygame.joystick.Joystick(0)
 joystick.init()

def setup_channels(channels):
 io.setmode(io.BCM)
 io.setwarnings(False)
 io.setup(channels,io.OUT)

def setup_pwm():
 global pwm_motor1
 global pwm_motor2
 global pwm_servo
 pwm_motor1 = io.PWM(9,100)    
 pwm_motor2 = io.PWM(10,100)  
 pwm_servo = io.PWM(26,50)  
 pwm_motor1.start(0)       
 pwm_motor2.start(0)      
 pwm_servo.start(0)  

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
 pwm_motor1.ChangeDutyCycle(5)
 io.output(11,0)
 io.output(17,1)
 io.output(22,1)
 io.output(27,0)

def forwardRight():
 pwm_motor2.ChangeDutyCycle(5)
 io.output(11,0)
 io.output(17,1)
 io.output(22,1)
 io.output(27,0)

def backwardLeft():
 pwm_motor1.ChangeDutyCycle(5)
 io.output(11,1)
 io.output(17,0)
 io.output(22,0)
 io.output(27,1)

def backwardRight():
 pwm_motor2.ChangeDutyCycle(5)
 io.output(11,1)
 io.output(17,0)
 io.output(22,0)
 io.output(27,1)

def pwmGearZero():
 pwm_motor1.ChangeDutyCycle(0)
 pwm_motor2.ChangeDutyCycle(0)

def pwmGearOne():
 pwm_motor1.ChangeDutyCycle(30)
 pwm_motor2.ChangeDutyCycle(30)

def pwmGearTwo():
 pwm_motor1.ChangeDutyCycle(50)
 pwm_motor2.ChangeDutyCycle(50)

def pwmGearThree():
 pwm_motor1.ChangeDutyCycle(75)
 pwm_motor2.ChangeDutyCycle(75)

def pwmGearFour():
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
 global pwm_stick
 
 if not joystick.get_button(R2) and not joystick.get_button(L1) and not joystick.get_button(D_pad_right) and not joystick.get_button(D_pad_left) and joystick.get_axis(left_stick_LeftRight) > -0.1 and joystick.get_axis(left_stick_LeftRight) < 0.1:
  stop()
 if joystick.get_axis(left_stick_LeftRight) < -0.1 and joystick.get_button(R2):
  forwardLeft()
 if joystick.get_axis(left_stick_LeftRight) < -0.1 and joystick.get_button(L2):
  backwardLeft()
 if joystick.get_axis(left_stick_LeftRight) < -0.1 and not joystick.get_button(R2) and not joystick.get_button(L2):
  pwm_stick = 100 * joystick.get_axis(left_stick_LeftRight) * -1
  print pwm_stick
  pwm_motor1.ChangeDutyCycle(pwm_stick)
  pwm_motor2.ChangeDutyCycle(pwm_stick)
  left()
 if joystick.get_axis(left_stick_LeftRight) > 0.1 and joystick.get_button(R2):
  forwardRight()
 if joystick.get_axis(left_stick_LeftRight) > 0.1 and joystick.get_button(L2):
  backwardRight()
 if joystick.get_axis(left_stick_LeftRight) > 0.1 and not joystick.get_button(R2) and not joystick.get_button(L2):
  pwm_stick = 100 * joystick.get_axis(left_stick_LeftRight)
  print pwm_stick
  pwm_motor1.ChangeDutyCycle(pwm_stick)
  pwm_motor2.ChangeDutyCycle(pwm_stick)
  right()
 if joystick.get_button(R2):
  forward()
 if joystick.get_button(L2):
  backward()
  
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

def eventControl(e):
 global delay_print
 global counter_print
 
 if e.type == pygame.QUIT:
  crashed = True
 if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
  crashed = True

 if e.type == pygame.JOYBUTTONDOWN:
  if joystick.get_button(R2):
   print("forward")
  elif joystick.get_button(L2):
   print("backward")

 if e.type == pygame.JOYAXISMOTION:
  if counter_print >= delay_print:
   counter_print = 0
   if joystick.get_axis(left_stick_LeftRight) < -0.2 and joystick.get_button(R2):
    print("forwardleft")
   elif joystick.get_axis(left_stick_LeftRight) < -0.2 and joystick.get_button(L2):
    print("backwardleft")
   elif joystick.get_axis(left_stick_LeftRight) < -0.2:
    print("left")
   elif joystick.get_axis(left_stick_LeftRight) > 0.2 and joystick.get_button(R2):
    print("forwardright")
   elif joystick.get_axis(left_stick_LeftRight) > 0.2 and joystick.get_button(L2):
    print("backwardright")
   elif joystick.get_axis(left_stick_LeftRight) > 0.2:
    print("right")
   elif joystick.get_axis(right_stick_LeftRight) < -0.5:
    print("servo turning left")
   elif joystick.get_axis(right_stick_LeftRight) > 0.5:
    print("servo turning right")
  else:
   counter_print+=1

def GearControl():
 global counter_gear_switch
 if joystick.get_button(L1) and counter_gear_switch > delay_gear_switch:
  SwitchGearDown()
  counter_gear_switch = 0
 elif joystick.get_button(R1) and counter_gear_switch > delay_gear_switch:
  SwitchGearUp() 
  counter_gear_switch = 0
 else:
  counter_gear_switch+=1

def ServoControl():
 if joystick.get_axis(right_stick_LeftRight) < 0.2 and joystick.get_axis(right_stick_LeftRight) > -0.2:
  pwm_servo.ChangeDutyCycle(0)

 if joystick.get_axis(right_stick_LeftRight) > 0.2 and joystick.get_axis(right_stick_LeftRight) <= 0.8:
  pwm_servo.ChangeDutyCycle(pwm_servo_right_low)
 if joystick.get_axis(right_stick_LeftRight) > 0.8:
  pwm_servo.ChangeDutyCycle(pwm_servo_right_high)

 if joystick.get_axis(right_stick_LeftRight) < -0.2 and joystick.get_axis(right_stick_LeftRight) >= -0.8:
  pwm_servo.ChangeDutyCycle(pwm_servo_left_low)
 if joystick.get_axis(right_stick_LeftRight) < -0.8:
  pwm_servo.ChangeDutyCycle(pwm_servo_left_high)

def main():
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
