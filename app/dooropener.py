from flask import Flask
from flask import make_response
from flask import redirect, url_for
from flask import abort
from flask import render_template # You know to, to render stuff
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from pprint import pprint
from loginForm import LoginForm # So we can login... duh

"""
  Command Strings
  $axxx* // Open Door
  $bxxx* // Open Door Close
"""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a hard key'
app.config['testable'] ='This is a test'
bootstrap = Bootstrap(app)
manager = Manager(app)

@app.route('/', methods=['GET', 'POST'])
def index():
  form = LoginForm()
  print form.errors
  userName = None
  password = None
  if form.validate_on_submit() :
    print "This shit is valid"
    user = form.userName.data
  return render_template('user.html', form=form, userName=userName,password=password )

# Route with variable passed in from the get variable
@app.route('/user')
def user():
    return render_template('user.html')

# Route to authenticate users
@app.route('/auth', methods=['POST'])
def auth():
  creds={'siracObama':'teamonmyback', 'steven':'brbgolfing','alfred':'justchillin'}
  return "Hullo?"


if __name__ == "__main__":
    print "We're in main"
    manager.run()
