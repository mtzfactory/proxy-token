from flask import Flask, request, Response, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    origin = request.headers["Origin"]
    return jsonify({ "method" : request.method, "origin" : origin })

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)