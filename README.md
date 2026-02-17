# Arduino-Mouse-Controller
Control your mouse using arduino uno and joystick

Materials needed:
Arduino uno
Joystick module
5 Male to female wires

Steps:
1. Connect the joystick module pins to their corresponding pin holes in the arduino using the male to female wires
   (gnd to gnd, +5v to 5v, VRX to A0, VRY to A1, SW to 7).
2. Connect the arduino module to your laptop/computer.
3. After that run the arduino script, then the python script (You can check if the joystick is giving an input by checking the serial monitor).
4. After running the scripts you can now control your mouse using the joystick button.

mouse_arduino.ino:
This script reads off the x and y values of the joystick module as well as if the button is clicked.
Mouse.py:
This reads off of the data passed onto the arduino script using pyserial, it then translates it into mouse movements using pyautogui.
To terminate the program, simply move the mouse to one of the four corners of your screen. If you can't move the mouse, check the wires if some of them are loose, if not then simply disconnect to the arduino to your laptop/computer.
