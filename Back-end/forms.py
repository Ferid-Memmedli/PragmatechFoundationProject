from models import Category
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,SelectField,TextAreaField,FileField

class CategoryForm(FlaskForm):
    name=StringField('Category Name')
    submit=SubmitField()

class PortfolioForm(FlaskForm):
    title = StringField('Title Name')
    image = FileField('Photo')
    category = SelectField('Choose Categories',choices=Category.query.with_entities(Category.id,Category.name).all())
    submit=SubmitField()