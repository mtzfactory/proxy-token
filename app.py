from flask import Flask, request, Response, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    origin = 'no-set'
    language = 'no-set'
    host = 'no-set'

    if request.headers.get('Origin'):
        origin = request.headers['Origin']

    if request.headers.get('Accept-Language'):
        language = request.headers['Accept-Language']

    if request.headers.get('Host'):
        language = request.headers['Host']

    return jsonify({ 
        'method' : request.method,
        'origin' : origin,
        'language' : language,
        'host' : host,
        'endpoint' : request.endpoint,
        'cookies' : request.cookies,
        'data' : request.data,
        'args' : request.args,
        'remote_addr' : request.remote_addr
    })

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)