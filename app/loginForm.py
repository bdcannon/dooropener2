from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, InputRequired

class LoginForm(Form):
  userName = StringField('User Name', validators=[InputRequired()])
  password = PasswordField("Password", validators=[InputRequired()])
  submit = SubmitField('Submit')
