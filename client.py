from helpers import *
from enum import Enum
from grovepi import *
from recording import *

class States(Enum):
  STARTUP = 1
  RECORDING = 2
  IDLE = 3

state = States.STARTUP

STARTUP_MSG = "Welcome to AudioGPT, an audio interface for accessing ChatGPT!"

if __name__ == "__main__":
  try:
    while True:
      if state == States.STARTUP:
        setup()
        scrollText(STARTUP_MSG)

        state = States.IDLE

      elif state == States.IDLE:
        BUTTON_STATE = digitalRead(BUTTON_PIN)

        if (BUTTON_STATE):
          state = States.RECORDING

      elif state == States.RECORDING
          while checkButton(BUTTON_PIN):
            # Polling to debounce button

          # Start LED to indicate recording in process
          digitalWrite(RED_LED_PIN, 1)

          record(checkButton, BUTTON_PIN)

          # Turn off Recording Status LED
          digitalWrite(RED_LED_PIN, 0)

          scrollText("Processing Recording")

          state = States.IDLE



  except KeyboardInterrupt:
    print("\n" + "Service ended.")

