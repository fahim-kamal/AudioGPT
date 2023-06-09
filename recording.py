import sounddevice as sd
import soundfile as sf
import queue
import os

# Documentation with example for recording for indefinite duration 
# https://python-sounddevice.readthedocs.io/en/0.4.6/examples.html#recording-with-arbitrary-duration

fs = 44100  # Sample rate
MICROPHONE = "USB PnP Sound Device" # Name of the particular microphone attached to RPI

q = queue.Queue()
path = "./output.wav" # Output file

def callback(indata, frames, time, status):
    q.put(indata.copy())

def record(checkButton, PIN):
    try:
        doesFileExist = os.path.isfile(path)

        if doesFileExist:
            os.remove(path)

        with sf.SoundFile("output.wav", mode='x', samplerate=fs, channels=1) as file:
            with sd.InputStream(samplerate=fs, device=MICROPHONE, channels=1, callback=callback):
                while checkButton(PIN) == False:
                    file.write(q.get())

    except KeyboardInterrupt:
        print("Recording Finished")




