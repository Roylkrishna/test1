from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Allow requests from your Vercel frontend (replace URL after deployment)
CORS(app, origins=["*"])  

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask backend on PythonAnywhere!"})

if __name__ == "__main__":
    app.run()
