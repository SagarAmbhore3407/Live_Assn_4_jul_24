
#39.  How would you create a basic Flask route that displays "Hello, World!" on the homepage?

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<H1>Hello World!</H1>"


if __name__ == "__main__":
    app.run(debug = True)