import time
from flask import Flask,request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/circuit", methods=['GET'])
@cross_origin()
def returnapp():
    return "App is UP!!"


@app.route("/circuit/good", methods=['GET'])
@cross_origin()
def return_good():
    return "ok you are getting http 200", 200


@app.route("/circuit/internal", methods=['GET'])
@cross_origin()
def return_internal_error():
    return "error :: internal server", 500


@app.route("/circuit/gateway", methods=['GET'])
@cross_origin()
def return_gateway():
    return "error :: Gateway Timeout", 504


@app.route("/circuit/service", methods=['GET'])
@cross_origin()
def return_service_error():
    return "error :: service unavailable", 503


@app.route("/circuit/delay", methods=['GET'])
@cross_origin()
def return_delay():
    delay = request.args.get('time')

    time.sleep(int(delay))
    return "returning response after :: " + delay + " secs", 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9000)
