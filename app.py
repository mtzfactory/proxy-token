# import os
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello World!'

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def homepage():
#    if request.environ['HTTP_ORIGIN'] is not None:
#        origin = request.environ['HTTP_ORIGIN']

    return request.method

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)