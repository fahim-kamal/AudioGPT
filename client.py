from helpers import *
from enum import Enum
from grovepi import *

class States(Enum):
  STARTUP = 1
  RECORDING = 2
  IDLE = 3

state = States.STARTUP

STARTUP_MSG = "Welcome to AudioGPT, an audio interface for accessing ChatGPT!"

if __name__ == "__main__":
  while True:
    if state == States.STARTUP:
      setup()
      scrollText(STARTUP_MSG)

      state = States.IDLE
    elif state == States.IDLE:
      BUTTON_STATE = digitalRead(BUTTON_PIN)

      if (BUTTON_STATE):
        scrollText("You have clicked the button!")


