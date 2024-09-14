from flask import Flask, request, redirect, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Serve index.html from the current directory
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    if not query:
        return redirect('/')
    url = f'https://www.google.com/search?q={query}'
    return redirect(url)

if __name__ == '__main__':
    app.run(port=8000)
