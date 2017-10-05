from flask import Flask, request, Response, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    origin = 'no-set'
    language = 'no-set'

    if request.headers.get("Origin"):
        origin = request.headers["Origin"]

    if request.headers.get("Accept-Language"):
        language = request.headers["Accept-Language"]

    return jsonify({ "method" : request.method, "origin" : origin, "language" : language })

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)