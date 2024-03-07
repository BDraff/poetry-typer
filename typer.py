import pyautogui
import time
import sys

# Give yourself a few seconds to switch to the window where you want to send keystrokes

filename = sys.argv[1]
print(filename)

with open(filename) as poem_file:
	print(" -- Waiting a few seconds -- ")

	time.sleep(3)
	while True:
		line = poem_file.readline()
		if len(line) < 1:
			break
		time.sleep(3)
		# Typing the text
		pyautogui.typewrite(line)

# Pressing the Enter key
pyautogui.press('')
