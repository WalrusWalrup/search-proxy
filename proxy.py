from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def proxy():
    url = request.args.get('url')
    if not url:
        return 'Missing URL parameter', 400

    # Ensure the URL starts with http or https
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    # Redirect to the specified URL
    return redirect(url)

if __name__ == '__main__':
    app.run(port=8000)
