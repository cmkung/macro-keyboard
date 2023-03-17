import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


keyboard = Keyboard(usb_hid.devices)


copypast_pin = board.GP19
back_pin = board.GP18

copypast = digitalio.DigitalInOut(copypast_pin)
copypast.direction = digitalio.Direction.INPUT
copypast.pull = digitalio.Pull.DOWN

back = digitalio.DigitalInOut(back_pin)
back.direction = digitalio.Direction.INPUT
back.pull = digitalio.Pull.DOWN

print('start...')
while True:
    if copypast.value:  
        print(" copypast button Pressed")
        keyboard.press(Keycode.LEFT_CONTROL)
        keyboard.press(Keycode.V)
        time.sleep(0.15)
        keyboard.release(Keycode.LEFT_CONTROL)
        keyboard.release(Keycode.V)
        
    if back.value:  
        print(" back button Pressed")
        keyboard.press(Keycode.LEFT_CONTROL)
        keyboard.press(Keycode.Z)
        time.sleep(0.15)
        keyboard.release(Keycode.LEFT_CONTROL)
        keyboard.release(Keycode.Z)
        
    time.sleep(0.1)
