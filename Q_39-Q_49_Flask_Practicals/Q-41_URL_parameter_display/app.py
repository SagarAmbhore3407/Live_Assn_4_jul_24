

# 41.Write a Flask route that accepts a parameter in the URL and displays it on the page.


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Home Page!'

@app.route('/display/<parameter>')
def display(parameter):
    return f'<h1>The parameter you provided is: {parameter}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
