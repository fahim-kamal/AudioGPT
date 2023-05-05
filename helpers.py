from grovepi import *
from grove_rgb_lcd import *
import time

RED_LED_PIN = 7
BUTTON_PIN = 2

def setup() -> None:
  pinMode(RED_LED_PIN, "OUTPUT")
  pinMode(BUTTON_PIN, "INPUT")

def scrollText(text: str) -> None: 
  # Set up backlight
  # setRGB(124, 242, 0)

  # Split up text into easily scrollable elements
  partions = text.split(' ')

  lines = [];

  while len(partions) != 0:
    line1 = ""
    new_length = len(partions[0])

    while new_length <= 16 and len(partions) != 0:
      if len(line1) != 0 and len(line1) <= 15:
        line1 += " "

      new_length = len(line1) + len(partions[0])

      if (new_length <= 16):
        line1 += partions[0]
        partions.pop(0)
    
    line1.ljust(16)
    lines.append(line1)
  
  # Output Text
  for i in range(len(lines)):
    if (len(lines) - i) >= 2:
      setText_norefresh(lines[i].ljust(16) + lines[i+1].ljust(16))
    else:
      setText_norefresh(lines[i].ljust(16) + "".ljust(16))

    time.sleep(1)


def checkButton(PIN):
  button_state = digitalRead(PIN)

  return button_state

scrollText("Hi, welcome to your new virtual assistant!")