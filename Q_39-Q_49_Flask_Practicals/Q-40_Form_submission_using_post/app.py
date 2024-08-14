
#  40.Explain how to set up a Flask application to handle form submissions 
#     using POST requests.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return f'<h2>Thank you, {name}! Your email {email} has been submitted.</h2>'

if __name__ == '__main__':
    app.run(debug=True)
