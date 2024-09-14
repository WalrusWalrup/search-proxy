from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proxy Search</title>
</head>
<body>
    <h1>Proxy Search</h1>
    <form action="/redirect" method="get">
        <input type="text" name="url" placeholder="Enter URL here" size="50" autofocus>
        <button type="submit">Go</button>
    </form>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/redirect')
def redirect_to_url():
    url = request.args.get('url')
    if not url:
        return 'Missing URL parameter', 400
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return redirect(url)

if __name__ == '__main__':
    app.run(port=8000)
