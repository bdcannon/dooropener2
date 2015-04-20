from flask import Flask
from flask import make_response
from flask import abort
from flask import render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hellow World</h1>'

# Route with variable passed in from the get variable
@app.route('/user')
def user():
    return render_template('user.html')


if __name__ == "__main__":
    print "We're in main"
    #app.run(debug=True)
    manager.run()
