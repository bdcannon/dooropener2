from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, InputRequired

class LoginForm(Form):
  userName = StringField('What is your name?', validators=[InputRequired()])
  password = PasswordField("What is your password?", validators=[InputRequired()])
  submit = SubmitField('Submit')
