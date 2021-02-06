from models import Category
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,FileField,PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class CategoryForm(FlaskForm):
    name=StringField('Category Name')
    submit=SubmitField()

class PortfolioForm(FlaskForm):
    title = StringField('Portfolio Name')
    image = FileField('Portfolio Image')
    category = SelectField('Choose Categories',choices=Category.query.with_entities(Category.id,Category.name).all())
    submit=SubmitField()



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=25),DataRequired()])
    email = StringField('Email Address', validators=[Email(),DataRequired()])
    password = PasswordField('New Password',
        validators=[DataRequired(),
        EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit=SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=25),DataRequired()])
    password = PasswordField('New Password',validators=[DataRequired()])
    submit=SubmitField('Login')
