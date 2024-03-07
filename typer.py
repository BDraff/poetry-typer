import pyautogui
import time
import sys

filename = sys.argv[1]
print(f"Reading File: {filename}")


def type_with_pause(text, pause_duration=0.3):
    words = text.split()  # Split the text into words
    if len(words) == 0:
        return
    for word in words[:-1]:
        pyautogui.typewrite(word)  # Type the word
        pyautogui.press('space')  # Simulate pressing the spacebar
        time.sleep(pause_duration)  # Pause between each word
    pyautogui.typewrite(words[-1])  # Type the word
    pyautogui.press('enter')  # Simulate pressing the spacebar


with open(filename) as poem_file:
    print(" -- Waiting a few seconds -- ")
    # Give yourself a few seconds to switch to the window where you want to send keystrokes
    time.sleep(3)
    for line in poem_file:
        if '#' in line: # Remove markdown comments
            continue
        type_with_pause(line)

        # Pause between lines
        time.sleep(3)

time.sleep(0.1)

# Pressing the Enter key
# pyautogui.press('Enter')
