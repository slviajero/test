import os

from flask import Flask, request
from main import eulers_reply

app = Flask(__name__)

@app.route('/')
def hello_world():
    target=request.args.get('message',default=1000, type=int)
    return eulers_reply(target)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
