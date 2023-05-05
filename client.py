from helpers import *
from enum import Enum
from grovepi import *
from recording import *
import time
import requests

SERVER_URL = "http://172.20.10.2:5000"

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
        setText_norefresh("Waiting for input".ljust(32))

        BUTTON_STATE = digitalRead(BUTTON_PIN)

        if (BUTTON_STATE):
          state = States.RECORDING

      elif state == States.RECORDING:
          while checkButton(BUTTON_PIN):
            # Polling to debounce button
            time.sleep(0.001)

          # Start LED to indicate recording in process
          digitalWrite(RED_LED_PIN, 1)
          setRGB(255,160,122)

          record(checkButton, BUTTON_PIN)

          # Turn off Recording Status LED and update LCD
          digitalWrite(RED_LED_PIN, 0)
          setText_norefresh("Processing".ljust(16) + "Recording".ljust(16))

          # Send file to server
          with open('output.wav', 'rb') as file:
            res = requests.post(SERVER_URL + "/upload", files={"audio": file})

            scrollText(res.json()['text'])

          state = States.IDLE



  except KeyboardInterrupt:
    print("\n" + "Service ended.")

