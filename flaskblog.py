from flask import Flask, render_template

app = Flask(__name__)
# (__name__) is a special variable in python that is just the name of the module

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

# we need to set an environment variable to the file that we want to be our flask application.
# (in this case) 
# $ export FLASK_APP=flaskblog.py

# OR add the next two lines and run the app with python command

# if __name__ == '__main__':
# 	app.run(debug=True)