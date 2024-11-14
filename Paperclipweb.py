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

@app.route('/get_count', methods=['GET'])
def get_count():
    global counter
    return jsonify(counter=counter)

if __name__ == '__main__':
    app.run(debug=True)
