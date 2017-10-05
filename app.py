from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return request.method

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)