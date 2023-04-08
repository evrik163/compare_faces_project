from flask import Flask
from flask import request
from face_rec_logic import mini_api


app = Flask(__name__)


@app.route("/json_example", methods=["POST", "GET"])
def json_example():
    return "Result of comparing faces: {}".format(mini_api(
                                                  request.get_json()
                                                  ))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
