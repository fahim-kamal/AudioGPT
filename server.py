from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/upload", methods=['POST'])
def upload_file():
    uploaded_file = request.files['audio']

    with open("output.wav", "wb") as binary_file:
        binary_file.write(upload_file)

