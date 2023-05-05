from flask import Flask, request, jsonify
import subprocess, json
import API

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

    text = API.askChatGPT(result)

    res = {"text": text}

    return jsonify(res), 200

@app.route("/delay", methods=['POST'])
def upload_delay():
    with open("output.txt", "at") as file:
        data = request.get_json(force=True)
        data = json.loads(data)
        file.write(data["text"])
        file.write(data["delay"])

    return "Success", 200

