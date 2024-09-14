from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', query=None)

@app.route('/search')
def search():
    query = request.args.get('q')
    return render_template('index.html', query=query)

if __name__ == '__main__':
    app.run(port=8000)
