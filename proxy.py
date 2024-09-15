from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    url = f'http://example.com/{path}'
    response = requests.get(url, params=request.args)
    return response.text

if __name__ == '__main__':
    app.run(port=8080)