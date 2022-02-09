from flask import Flask, render_template, url_for, flash, redirect
# all of the above are flask tools for developing
from forms import RegistrationForm, LoginForm
import os

app = Flask(__name__)
# (__name__) is a special variable in python that is just the name of the module
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

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