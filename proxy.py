from flask import Flask, request, Response, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return 'Missing URL parameter', 400

    try:
        response = requests.get(url)
        return Response(response.content, content_type=response.headers.get('Content-Type'))
    except requests.RequestException as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(port=8000)
