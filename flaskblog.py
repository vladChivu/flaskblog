from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
# all of the above are flask tools for developing
from forms import RegistrationForm, LoginForm
import os

app = Flask(__name__)
# (__name__) is a special variable in python that is just the name of the module
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# not a good idea to sit here, the sql file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# creates a db instance

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    # relationship to the 'Post Model';
    # we wouldn't see this column in the database it just adds an additional Query on the Post table

    # backref is similar to adding another column to the 'Post' model so that when we have a Post
    # we can get it's author with this attribute that we passed in here

    # lazy justifies when sqlalchemy loads the data from the database so true means
    # that SQLAlchemy will load the data in one go

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    #how our object is printed whenever we printed out

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # we are not using the parentheses because we want to use that function as an argument so 
    # it will dinamycally run when it is called and that is when a Post class gets instantiated
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
	# return "Hello World!"
    # return "<h1>Hello World!</h1>"
    # return "<h1>Home Page</h1>"
    return render_template('home.html', posts=posts)
    # we will have access in our template to the posts variable

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
        # home here is the name of the function we want to redirect to
    return render_template('register.html', title="Registration", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful!', 'danger')
    return render_template('login.html', title="Login", form=form)

# we need to set an environment variable to the file that we want to be our flask application.
# (in this case) 
# $ export FLASK_APP=flaskblog.py

# OR add the next two lines and run the app with python command
# if __name__ == '__main__':
# 	app.run(debug=True)