from grovepi import *
from grove_rgb_lcd import *
import time

RED_LED_PIN = 7
BUTTON_PIN = 2
ROTARY_PIN = 0

class RotarySensor():
    def __init__(self, port):
        self.port = port
        self.ADC_REF = 5
        self.GROVE_VCC = 5
        self.FULL_ANGLE = 300
    
        pinMode(self.port, "INPUT")
        time.sleep(1)

    def read(self):
        sensor_value = analogRead(self.port)
        voltage = sensor_value * self.ADC_REF / 1023
        degrees = (voltage * self.FULL_ANGLE) / self.GROVE_VCC
        return round(degrees)

def calculateDelay(angle: int) -> int:
  # goes from 0.5 -> 5 seconds 
  return -0.015 * angle + 5 

def setup() -> None:
  pinMode(RED_LED_PIN, "OUTPUT")
  pinMode(BUTTON_PIN, "INPUT")

def scrollText(text: str, calcDelay, sensor: RotarySensor) -> None: 
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
    val = sensor.read()
    delay = calcDelay(val)

    if (len(lines) - i) >= 2:
      setText_norefresh(lines[i].ljust(16) + lines[i+1].ljust(16))
    else:
      setText_norefresh(lines[i].ljust(16) + "".ljust(16))

    time.sleep(delay)


def checkButton(PIN):
  button_state = digitalRead(PIN)

  return button_state

