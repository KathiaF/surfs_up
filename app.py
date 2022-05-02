# Import the Flask Dependency
from flask import Flask

# Create a New Flask App Instance
#  "Instance" is a general term in programming to refer to a singular version of something.
app = Flask(__name__)

# Create a Flask Routes
@app.route('/') #/: This denotes that we want to put our data at the root of our routes.
def hello_world():
        return 'Hello world'

# Run a Flask App
# terminal:
# export FLASK_APP=app.py
# set FLASK_APP=app.py
