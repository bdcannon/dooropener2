from flask import Flask
from flask import make_response
from flask import request
from flask import redirect, url_for
from flask import abort
from flask import session
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
app.config["CACHE_TYPE"] = "null"

# User Name and passwords. Not good to store in plain text like this but whatever
app.config['creds'] = {'siracObama':'teamonmyback',
                       'steven':'brbgolfing',
                       'alfred':'justchillin',
                       'ben': 'test'}

bootstrap = Bootstrap(app)
manager = Manager(app)

"""
    Route for the home page (index)
"""
@app.route('/', methods=['GET', 'POST'])
def index():
  form = LoginForm()
  userName = None
  password = None
  # Print out the stuff for a sanity check
  if form.validate_on_submit() :
    print "User Submitted User: %s\nPass:%s\n" % (form.userName.data, form.password.data)
    creds = app.config['creds'] # Get the credentials dictionary
    user = form.userName.data
    formPassword = form.password.data
    if user in creds :  # Check to see if the user name is in there
        storedPassword = creds[user]
        # Check the password
        if storedPassword == formPassword :
            session[user] = "!!!";
            return redirect("/controls?name="+user)
        else :
            form.password.data = '' # Clear the password data
            return render_template('index.html', form=form, userName=userName,password=password )
  return render_template('index.html', form=form, userName=userName, password=password)

"""
    Route to display controls
"""
@app.route('/controls', methods=["GET", "POST"])
def controls():
    user = request.args.get('name')
    # If remove is in the form then the user picked something
    if 'remove' in request.form :
        # Remove the session
        session.pop(user, None)
        print "the session is now"
        print session
    if user in session :
        return render_template('controls.html') # Renders the controls page
    else :
        return redirect(url_for('index'))

# Route to authenticate users
@app.route('/auth', methods=['POST'])
def auth():
  return "Hullo?"


if __name__ == "__main__":
    print "We're in main"
    manager.run()
