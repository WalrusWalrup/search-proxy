from flask import Flask, request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def proxy():
    url = request.args.get('url')
    if not url:
        return 'Missing URL parameter', 400

    # Validate and format the URL
    if not url.startswith('http'):
        url = 'http://' + url

    # Try to fetch the URL and handle errors
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return redirect(url)
        else:
            return 'Failed to fetch URL', response.status_code
    except requests.RequestException as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(port=8000)
