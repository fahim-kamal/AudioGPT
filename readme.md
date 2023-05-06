# AudioGPT

AudioGPT is a physical, audio interface for ChatGPT that uses the RaspberryPI and the GrovePI shield to communicate with ChatGPT through the use of just of a microphone.

### Quickstart:

Before you begin, configure your API keys for OpenAI and AssemblyAI in a .env file. API.py expects the OpenAI key to be called OPEN_AI_API_KEY and AssemblyAI's API key is configured through their CLI. AudioGPT requires the use of OpenAI's API for chat completion and AssemblyAI for voice transcription. Be sure to change the audio output device in recording.py to one avaiable on the RaspberryPi.

### Dependencies

See requirements.txt and download the grovepi packages for RPi (https://github.com/DexterInd/GrovePi).<br>
`python3 -m venv ./`<br>
`source ./bin/activate`<br>
`pip3 install -r requirements.txt`<br>

### Start up the server on a VM/local machine that is on the same wifi network as the RPi:

`python3 -m flask --app server run --host=0.0.0.0`

### Once the server is setup, run client.py on the RaspberryPI.

`python3 client.py`

### To output the visualization of the time delay for each step: [can be done without running server.py or client.py based on the history in output.txt]

`python3 out.py`

### Hardware

[GrovePI Connections](https://imgur.com/1EZ1apw)<br>

- Rotary Encoder: A0
- Button: D2
- Red LED: D7
- LCD Display: Any I2C Port

### Members:

- Fahim Kamal

### Link to Demo Video:

[https://docs.google.com/presentation/d/1Hqi-49sFnZNNGlGtmkeTU0-TbGNcMvXpPANK14By9Ww/edit?usp=sharing]
