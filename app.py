from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return { "method" : request.method, "headers" : "hola" } 

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)