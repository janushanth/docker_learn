#pip install flask 

from flask import Flask  #This imports Flask, a lightweight web framework for Python

app = Flask(__name__)    #Creates an instance of the Flask application. 
                        #__name__ tells Flask whether the script is run directly or imported.

@app.route('/')       #@app.route('/'): Defines a route (URL path)
def home():
    return "Hello, Small Kids!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)   #debug=True → Enables auto-restart on code changes and provides detailed error logs.
