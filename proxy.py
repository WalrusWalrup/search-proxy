from flask import Flask, request, Response, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy')
def proxy():
    search_term = request.args.get('url')
    if not search_term:
        return 'Missing search term parameter', 400

    search_url = f"https://www.bing.com/search?q={search_term}"
    return redirect(search_url)

if __name__ == '__main__':
    app.run(port=8000)
