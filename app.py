from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''<h1>Welcome to Website One</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>'''

if __name__ == '__main__':
    app.run(port=5000)