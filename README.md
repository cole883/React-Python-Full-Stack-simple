# full-stack-web-app-react-and-python
Creating a full-stack web application with Python, NPM, Webpack and React

<b>Step 1: Initial Project Setup</b>
<p>Start by creating the following directory structure inside your project folder:
  <br>├── README.md
  <br>└── fullstack_template/
  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── server/
  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── static/
  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── css/
  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── dist/
  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── images/
  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── js/
</p>

<b>Step 2: Let’s initialise the project: (Use CMD)</b>
<p>We will be using the npm package manager which will make it easy for our project dependencies to be up to date and install new packages.</p>
  
<p>
  Go to the static folder inside fullstack_template folder
  <br><pre>$ cd fullstack_template/static</pre>
</p>
<p>
  Initialise the npm package manager
  <br><pre>$ npm init</pre>
</p>
<p>
  Accept the default prompts, but fill in your application name and Git repository, if you have those available. Doing this will create a package.json file in your static directory.
  <br><br>You can update the anthor, license, description later
  <br><br>You package.jason file will look like this.
  <br><pre>
{
  "name": "fullstack_template",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "Danish",
  "license": "MIT"
}
  </pre>
</p>

<b>Step 3: Install and Configure Webpack</b>

<p>
  Install Webpack
  <br><pre>$ npm install webpack webpack-cli --save-dev</pre>
</p>
<p>
  To use webpack, we need to add a Webpack config file. The config tells webpack where to find the Javascript and React files, and where to put the generated Javascript bundle.
<br><br>Add a file named webpack.config.js in your static folder, with the following contents:
  <pre>
const webpack = require('webpack');
const config = {
    entry:  __dirname + '/js/index.jsx',
    output: {
        path: __dirname + '/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
};
module.exports = config;
  </pre>
</p>
<p>
  Add Run Commands
  
  <br>Adding a few run commands to the package.json file makes the development process more fluid. I always add build, dev-build and watch to my package.json
  
  <br>Here is my package.json
  <pre>
{
  "name": "FullStackTemplate",
  "version": "1.0.0",
  "description": "A Template for creating a Full Stack Web Application using Python, NPM, Webpack and React",
  "main": "index.js",
  "scripts": {
    "build": "webpack -p --progress --config webpack.config.js",
    "dev-build": "webpack --progress -d --config webpack.config.js",
    "test": "echo \"Error: no test specified\" && exit 1",
    "watch": "webpack --progress -d --config webpack.config.js --watch"
  },
  "keywords": [
    "fullstack",
    "template",
    "python",
    "react",
    "npm",
    "webpack"
  ],
  "author": "Danish",
  "license": "MIT",
  "devDependencies": {
    "webpack": "^4.39.3",
    "webpack-cli": "^3.3.7"
  }
}
  </pre>
</p>

<b>Step 4: Add Babel Support</b>

<p>
  Install Babel
  <br><pre>
$ npm install @babel/preset-env @babel/preset-react --save-dev
$ npm install babel-core babel-loader babel-preset-es2015 babel-preset-es2016 babel-preset-react --save-dev
$ npm install babel-loader@7 --save-dev
</pre>
</p>

<p>
  Add a babel-loader rule to the Webpack config. Note that we exclude node_modules. This will ensure that Babel does not try to transform any of our node modules, thereby speeding up the loader significantly.
  <br><pre>
module: {
  rules: [
    {
      test: /\.jsx?/,
      exclude: /node_modules/,
      use: 'babel-loader'
    }
  ]
}
  </pre>
</p>

<b>Step 5: Create index.jsx and index.html</b>

<p>
  In the static folder create the following index.html file and add a div with id "content" and add below script in the body
  <br><pre>
<script src="dist/bundle.js" type="text/javascript"></script>
</pre>
</p>

<p>
  In the static/js folder, create an index.jsx file with the following line:
  <br><pre>alert("Hello World!");</pre>
</p>

<p>
  Start the Webpack watch command we just created in a separate terminal tab. This means it can run in the background whilst we continue working. It should build your bundle without errors.
  <br><pre>npm run watch</pre>
</p>

<b>Step 6: Creating a Simple React App</b>

<p>
  First we need to install react.
  <br><pre>npm install react react-dom --save-dev</pre>
</p>

<p>
  Next we replace the alert in the index.jsx with a simple React app, and have it load a React class we have created in a separate App.js file.
  <br><pre>
// index.jsx
import React from "react"
import ReactDOM from "react-dom"

import App from "./App"

ReactDOM.render(<App />, document.getElementById("content"))
  </pre>
</p>

<p>
  React classes need to be exported to be importable in a different react file. It is common practice to only have one class per file, and export that file. Put Hello React! inside the paragraph tag
  <br><pre>
// App.jsx
import React from "react"

class App extends React.Component {
	render () { 
    return <p>Hello React!</p> 
  }
}

export default App
  </pre>
</p>

<p>
  See the watch CMD screen, You might get a Syntax Error in index.jsx file to fix this update your webpack.config.js module to this
  <br><pre>
module: {
  rules: [
    {
      test: /\.jsx?/,
      exclude: /node_modules/,
      use: [
        {
          loader: 'babel-loader',
          options: {
            presets: ['react']
          }
        }
      ]
    }
  ]
}
  </pre>
</p>

<b>Step 7: Configure the Python Server</b>

<p>
  For our Python server we will be using Flask. Flask is an excellent choice for small Python applications. The “microframework” is quick and easy to get started with, and you can get a server up and running in less than a minute. 
  
  <br>on Windows you will need to download the installer and run it manually so go here and download the python server from
  
  <br>Python: https://realpython.com/installing-python/#step-1-download-the-python-3-installer
</p>

<b>Step 8: Install Flask on server folder</b>

<p>Create a new Python virtualenv and install Flask.
  <br><pre>$ py -3 -m venv venv</pre>
</p>

<p>Activate the environment
  <br><pre>$ venv\Scripts\activate</pre>
</p>

<p>Install Flask
  <br><pre>$ pip install Flask</pre>
</p>

<p>Upgrade pip if asked
  <br><pre>$ python -m pip install --upgrade pip</pre>
</p>

<p>In the server directory, create the Flask server file. Add a “/hello” endpoint which will return “Hello World!” and a an index endpoint “/“ that will render the index.html template.  
  <br><pre>
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

//Run the program
$ py server.py
  </pre>
</p>

<p>Run the server.py file on server folder
  <br><pre>$ py server.py</pre>
</p>

<p>It will give you the URL to run the python on web browser, somthing like this
  <br><pre>Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)</pre>
</p>

<p>Now go to http://127.0.0.1:5000/ it will show you your react page
  <br><pre>Hello React!</pre>
</p>

<p>Add if you go to http://127.0.0.1:5000/hello it will show you your python page
  <br><pre>Hello World!</pre>
</p>
