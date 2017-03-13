from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired,Email,URL


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])

class ProductDetailForm(Form):
	product = StringField('product',validators=[DataRequired(),URL()])
