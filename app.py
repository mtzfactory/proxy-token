from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def homepage():
    headers = request.headers
    #.get('HTTP_ORIGIN', '').lower()

    return { "method" : request.method, "headers" : headers } 

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)