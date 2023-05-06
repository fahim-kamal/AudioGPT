from flask import Flask, request, jsonify
import subprocess, json, time, requests
import API

app = Flask(__name__)

SERVER_URL = "http://172.20.10.2:5000"

@app.route("/upload", methods=['POST'])
def upload_file():
    uploaded_file = request.files['audio'].read()

    with open("output.wav", "wb") as binary_file:
        binary_file.write(uploaded_file)

    start1 = time.time()
    result = subprocess.run(["assemblyai", "-f", "-j", "transcribe", "output.wav" ], capture_output=True, text=True)
    end1 = time.time()

    result = json.loads(result.stdout)
    result = result['text']

    start2 = time.time()
    text = API.askChatGPT(result)
    end2 = time.time()

    delays = {"question": result, "q_delay": end1 - start1, "answer": text, "a_delay": end2 - start2}

    requests.post(SERVER_URL + "/delay", json=json.dumps(delays))

    res = {"text": text}

    return jsonify(res), 200

@app.route("/delay", methods=['POST'])
def upload_delay():
    with open("output.txt", "at") as file:
        data = request.get_json(force=True)
        data = json.loads(data)
        file.write(data.get("question"))
        file.write("\n")
        file.write(str(data.get("q_delay")))
        file.write("\n")
        file.write(data.get("answer"))
        file.write("\n")
        file.write(str(data.get("a_delay")))
        file.write("\n")

    return "Success", 200

