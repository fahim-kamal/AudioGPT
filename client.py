from helpers import *
from enum import Enum
from grovepi import *
from recording import *
import time, requests, os

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
      rs = RotarySensor(ROTARY_PIN)
      delay = calculateDelay(rs.read())

      if state == States.STARTUP:
        setup()
        setRGB(124, 242, 0)
        scrollText(STARTUP_MSG, delay)

        state = States.IDLE

      elif state == States.IDLE:
        setRGB(255, 255, 0)
        setText_norefresh("Waiting for".ljust(16) + "your question!".ljust(16))

        BUTTON_STATE = digitalRead(BUTTON_PIN)

        if (BUTTON_STATE):
          while checkButton(BUTTON_PIN):
            # Polling to debounce button
            time.sleep(0.005)

          state = States.RECORDING

      elif state == States.RECORDING:
          # Start LED to indicate recording in process
          digitalWrite(RED_LED_PIN, 1)
          setRGB(255,0,0)
          setText("Recording...")

          record(checkButton, BUTTON_PIN)

          # Turn off Recording Status LED and update LCD
          digitalWrite(RED_LED_PIN, 0)
          setRGB(255,255,0)
          setText_norefresh("Processing".ljust(16) + "Recording".ljust(16))

          # Send file to server
          with open('output.wav', 'rb') as file:
            res = requests.post(SERVER_URL + "/upload", files={"audio": file})

            setRGB(124, 242, 0)
            scrollText(res.json()['text'], delay)

          state = States.IDLE



  except KeyboardInterrupt:
    os.remove("./output.wav")
    setRGB(0,0,0)
    setText("".ljust(32))
    print("\n" + "Service ended.")

