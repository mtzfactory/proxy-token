from flask import Flask, request, Response, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    origin = 'no-set'
    language = 'no-set'
    host = 'no-set'
    remote = 'no-set'
    server = 'no-set'

    if request.headers.get('Origin'):
        origin = request.headers['Origin']

    if request.headers.get('Accept-Language'):
        language = request.headers['Accept-Language']

    if request.headers.get('Host'):
        language = request.headers['Host']

    if request.environ.get('REMOTE_ADDR'):
        remote = request.environ['REMOTE_ADDR']

    if request.environ.get('SERVER_ADDR'):
        server = request.environ['SERVER_ADDR']

    return jsonify({
        'origin' : origin,
        'language' : language,
        'host' : host,
        'method' : request.method,
        'endpoint' : request.endpoint,
        'cookies' : request.cookies,
        # 'data' : request.data,
        'args' : request.args,
        'remote_addr' : request.remote_addr,
        'form' : request.form,
        'headers' : dict(request.headers),
        'url': request.url,
        'path' : request.path,
        'remote' : remote,
        'server' : server,
        # 'environ': dict(request.environ),
        # 'query_string' : request.query_string
    })

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)

# http://flask.pocoo.org/docs/0.12/api/#incoming-request-data
# http://flask.pocoo.org/docs/0.12/quickstart/#accessing-request-data