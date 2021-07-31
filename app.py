from flask import Flask
from flask import json
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    logging.info(" / endpoint was reached")
    return "Hello World!"

@app.route("/status")
def health():
    logging.info(" /status endpoint was reached")
    response = app.response_class(
        response = json.dumps({"result": "OK - healthy"}),
        status = 200,
        mimetype = "application/json"
    )
    return response    

@app.route("/metrics")
def metrics():
    logging.info(" /metrics endpoint was reached")
    response = app.response_class(
        response = json.dumps({"status":"success","data": {"UserCount": 140, "UserCountActive": 23}}),
        status = 200,
        mimetype = "application/json"
    )
    return response
    return "data: {UserCount: 140, UserCountActive: 23}"    

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
    app.run(host='0.0.0.0')
