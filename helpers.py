from grovepi import *
from grove_rgb_lcd import *
import time

LED_PIN = 7
BUTTON_PIN = 2

def setup() -> None:
  pinMode(LED_PIN, "OUTPUT")
  pinMode(BUTTON_PIN, "INPUT")

def scrollText(text: str) -> None: 
  # Set up backlight
  setRGB(124, 242, 0)

  # Split up text into easily scrollable elements
  partions = text.split(' ')

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
    line2 = "".ljust(16)

    # Output Text
    setText_norefresh(line1 + line2)
    time.sleep(1)

