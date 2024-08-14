
# 45.Explain how to use Flask-WTF to create and validate forms in a Flask application.

from flask import Flask, render_template, flash, redirect, url_for
from forms import MyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'  # Set a secret key for CSRF protection

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        flash('Form successfully submitted!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
