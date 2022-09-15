import os
from flask import Flask, request
from functions import do_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query():
    try:
        data = request.json
        file_name = data['file_name']
        os.path.join(DATA_DIR, file_name)
    except Exception as e:
        return e, 400

    return do_query(data)
    # return app.response_class('', content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
