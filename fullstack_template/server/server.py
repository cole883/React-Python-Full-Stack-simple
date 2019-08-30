# server.py
# Import the Flask class. An instance of this class will be our WSGI application.
from flask import Flask, render_template

# Next we create an instance of this class. The first argument is the name of the application’s module or package. 
# If you are using a single module (as in this example), you should use name because depending on if 
# it’s started as application or imported as module the name will be different ('main' versus the actual import name). 
# This is needed so that Flask knows where to look for templates, static files, and so on.
app = Flask(__name__, static_folder="../static/dist", template_folder="../static")

# We then use the route() decorator to tell Flask what URL should trigger our function.
# The function is given a name which is also used to generate URLs for that particular function, 
# and returns the message we want to display in the user’s browser.
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/hello")
def hello():
	return "Hello World!"

if __name__ == "__main__":
	app.run()