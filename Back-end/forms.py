from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,SelectField,TextAreaField

class RegForm(FlaskForm):
    name=StringField('Your Name')
    surname=StringField('Your Surname')
    submit=SubmitField()
