from flask import Flask, request, Response, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy')
def proxy():
    query = request.args.get('query')
    if not query:
        return 'Missing search query parameter', 400

    search_url = f"https://duckduckgo.com/?q={query}"
    return redirect(search_url)

if __name__ == '__main__':
    app.run(port=8000)
