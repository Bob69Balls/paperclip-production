import os
from flask import Flask, render_template, jsonify
import threading

app = Flask(__name__)

# Initialize a global counter
counter = 0
lock = threading.Lock()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/increment', methods=['POST'])
def increment():
    global counter
    with lock:
        counter += 1
    return jsonify(counter=counter)

@app.route('/')
def home():
    return "Hello, Render!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use port 10000 or the port provided by Render
    app.run(host="0.0.0.0", port=port)
