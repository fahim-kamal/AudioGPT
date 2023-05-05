from flask import Flask, request
import subprocess, json
from API import askChatGPT

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/upload", methods=['POST'])
def upload_file():
    uploaded_file = request.files['audio'].read()

    with open("output.wav", "wb") as binary_file:
        binary_file.write(uploaded_file)

    result = subprocess.run(["assemblyai", "-f", "-j", "transcribe", "output.wav" ], capture_output=True, text=True)

    result = json.loads(result.stdout)
    result = result['text']

    text = askChatGPT(result)

    return text, 200
