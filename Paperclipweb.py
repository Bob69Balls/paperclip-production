import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Render!"

if __name__ == "__main__":
    # Render expects the application to listen on the port defined in the PORT environment variable
    port = int(os.environ.get("PORT", 10000))  # Use Render's PORT or 10000 as a default
    app.run(host="0.0.0.0", port=port)
