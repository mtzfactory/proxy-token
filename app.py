import urllib.parse
import base64
import json
from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from httplib2 import Http

app = Flask(__name__)
cors = CORS(app, resources = { r"/api/*" : { "origins" : "*" } })
         
apiKey = 'aaaabbbbccccddddeeeeffffgggghhhh'
apiSecret = 'aaaabbbbccccddddeeeeffffgggghhhh'

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

@app.route('/api/v1/mtzfactory')
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