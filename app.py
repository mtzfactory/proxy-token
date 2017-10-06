import urllib.parse
import base64
import json
from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from httplib2 import Http

app = Flask(__name__)

apiKey = '8eb8889dad5d4a4f8fa4ec40e472cb6d'
apiSecret = 'ac64eda063e247ee933c6e7e298df0b1'

app.config['CORS_HEADERS'] = 'Content-Type'

def getOauthToken(apiKey, apiSecret):
    url = 'https://accounts.spotify.com/api/token'
    #---
    http_obj = Http()
    auth = apiKey + ':' + apiSecret
    auth64 = base64.b64encode(auth.encode("utf-8"))
    body = { 'grant_type':'client_credentials' }
    headers = { 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Authorization' : 'Basic ' + auth64.decode('utf-8') }
    resp, content = http_obj.request(url, method = 'POST', headers = headers, body = urllib.parse.urlencode(body))
    return resp, json.loads(content)

@app.route('/')
@cross_origin()
def index():
    host = 'no-set'
    client = 'no-set'

    if request.headers.get('Host'):
        host = request.headers['Host']

    if request.headers.get('X-Forwarded-For'):
        client = request.headers['X-Forwarded-For']

    r, t = getOauthToken(apiKey, apiSecret)
    return jsonify({
        'client' : client,
        'token': t['access_token']
        })

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)

# http://flask.pocoo.org/docs/0.12/api/#incoming-request-data
# http://flask.pocoo.org/docs/0.12/quickstart/#accessing-request-data

    # origin = 'no-set'
    # language = 'no-set'
    # remote = 'no-set'
    # server = 'no-set'

    # if request.headers.get('Origin'):
    #     origin = request.headers['Origin']

    # if request.headers.get('Accept-Language'):
    #     language = request.headers['Accept-Language']

    # if request.environ.get('SERVER_ADDR'):
    #     server = request.environ['SERVER_ADDR']

    # if request.environ.get('REMOTE_ADDR'):
    #     remote = request.environ['REMOTE_ADDR']

    # return jsonify({
    #     'origin' : origin,
    #     'language' : language,
    #     'host' : host,
    #     'method' : request.method,
    #     'endpoint' : request.endpoint,
    #     'cookies' : request.cookies,
    #     # 'data' : request.data,
    #     'args' : request.args,
    #     'remote_addr' : request.remote_addr,
    #     'form' : request.form,
    #     'headers' : dict(request.headers),
    #     'url': request.url,
    #     'path' : request.path,
    #     'remote' : remote,
    #     'server' : server,
    #     # 'environ': dict(request.environ),
    #     # 'query_string' : request.query_string
    # })