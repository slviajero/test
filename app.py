import os

from flask import Flask, request
from main import eulers_dream

app = Flask(__name__)

@app.route('/')
def hello_world():
    return eulers_dream(request)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
