import os

from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
  return send_file('src/index.html')

@app.route("/hello")
def hello():
    return "Hello World!"

if __name__ == "__main__":
  app.run(port=int(os.environ.get('PORT', 8001)), debug=True)
