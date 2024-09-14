from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proxy Search</title>
    <script>
        function submitForm(event) {
            event.preventDefault();
            var url = document.getElementById('url').value;
            if (url) {
                if (!url.startsWith('http://') && !url.startsWith('https://')) {
                    url = 'http://' + url;
                }
                window.location.href = url;
            }
        }
    </script>
</head>
<body>
    <h1>Proxy Search</h1>
    <form onsubmit="submitForm(event)">
        <input type="text" id="url" placeholder="Enter URL here" size="50" autofocus>
        <button type="submit">Go</button>
    </form>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(port=8000)
