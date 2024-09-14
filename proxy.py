from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def proxy():
    url = request.args.get('url')
    if not url:
        return 'Missing URL parameter', 400
    
    # Validate the URL
    if not url.startswith('http'):
        url = 'http://' + url

    try:
        response = requests.get(url)
        return Response(response.content, content_type=response.headers['Content-Type'])
    except requests.RequestException as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(port=8000)
