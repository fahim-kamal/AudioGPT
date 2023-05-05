from helpers import *
from enum import Enum

class States(Enum):
  STARTUP = 1
  RECORDING = 2
  IDLE = 3

state = States.STARTUP

STARTUP_MSG = "Welcome to AudioGPT, an audio interface to accessing ChatGPT!"

if __name__ == "__main__":
  while True:
    if state == States.STARTUP:
      setup()
      scrollText(STARTUP_MSG)


