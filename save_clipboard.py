from PIL import ImageGrab
from datetime import datetime
from pynput import keyboard

current_pressed = set()
save_hot_key = set([keyboard.Key.alt_l, keyboard.Key.f12])

def save_image():
    img = ImageGrab.grabclipboard()
    filename = datetime.now().strftime('screenshot_%Y_%m_%d_%H_%M_%S')
    try:
        img.save(f"c:\Desktop\{filename}.png")
    except:
        pass

def on_press(key):
    current_pressed.add(key)
    if current_pressed & save_hot_key == save_hot_key:
        save_image()
        current_pressed.clear()
    
def on_release(key):
    if key in current_pressed:
        current_pressed.remove(key)
    
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
