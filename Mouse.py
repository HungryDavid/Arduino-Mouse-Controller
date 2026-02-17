import serial as s
import time as t
import pyautogui as mouse_control

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

mouse_control.FAILSAFE = True
mouse_control.PAUSE = 0 
mouse_control.MINIMUM_DURATION = 0
arduino = s.Serial(port='COM12', baudrate=115200, timeout=.1) 
t.sleep(2)
try:
  button_was_pressed = False
  while True:
    if arduino.in_waiting > 0:
      data = arduino.readline().decode('utf-8', errors='ignore').strip()
    if data:
      try:
        rx,ry = 954, 540
        x, y, btn = map(int, data.split(","))
        x = int((x / 1023) * SCREEN_WIDTH)
        y = int((y / 1023) * SCREEN_HEIGHT)
        lx = x - rx
        ly = y - ry
        print(f"X: {x:<5} | Y: {y:<5} | Button: {btn} | lx: {lx} | ly: {ly}")	
        mouse_control.moveRel(lx * 0.002,ly * 0.002)
        if btn == 0:
          if not button_was_pressed:
            mouse_control.click()
            button_was_pressed = True
        else:
          button_was_pressed = False
      except ValueError:
        print(f"Malformed data received: {data}")
except KeyboardInterrupt:
  print("\nStopping...")
finally:
  arduino.close()