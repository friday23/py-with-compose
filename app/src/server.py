from flask import Flask
import ptvsd

ptvsd.enable_attach(address=('0.0.0.0', 5678))

server = Flask(__name__)

@server.route("/")
def hello():
  return "Hello World\n"

if __name__ == "__main__":
  server.run(debug=True,host='0.0.0.0', port=5000)

