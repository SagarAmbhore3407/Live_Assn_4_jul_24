
#  49. Make a fully functional web application using flask, Mangodb. Signup,Signin page.And after successfully 
# login .Say hello Geeks message at webpage.


from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from forms import SignupForm, SigninForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/myDatabase'
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        
        user = mongo.db.users.find_one({'username': username})
        if user:
            flash('Username already exists')
            return redirect(url_for('signup'))
        
        mongo.db.users.insert_one({'username': username, 'password': password})
        flash('Signup successful! Please sign in.')
        return redirect(url_for('signin'))
    
    return render_template('signup.html', form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = mongo.db.users.find_one({'username': username})
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            flash('Login successful!')
            return redirect(url_for('home'))
        flash('Invalid credentials')
    
    return render_template('signin.html', form=form)

@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
