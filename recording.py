import sounddevice as sd
import soundfile as sf
import queue

fs = 44100  # Sample rate
MICROPHONE = "USB PnP Sound Device"

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(indata.copy())

try:
    with sf.SoundFile("output.wav", mode='x', samplerate=fs, channels=1) as file:
        with sd.InputStream(samplerate=fs, device=MICROPHONE, channels=1, callback=callback):
            while True:
                file.write(q.get())

except KeyboardInterrupt:
    print("Recording Finished")

