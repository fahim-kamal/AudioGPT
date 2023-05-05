import sounddevice as sd
import soundfile as sf
import queue
from scipy.io.wavfile import write
import time

fs = 44100  # Sample rate
# seconds = 30  # Duration of recording

# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)

# time.sleep(5)

# sd.stop()

# mic = "USB PnP Sound Device"

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(indata.copy())

try:
    with sf.SoundFile("output.wav", mode='x', samplerate=fs, channels=2) as file:
        with sd.InputStream(samplerate=fs, device=0, channels=2, callback=callback):
            while True:
                file.write(q.get())
except KeyboardInterrupt:
    print("Recording Finished")

