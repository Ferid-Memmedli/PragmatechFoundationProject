from app import app,db
from forms import *
from models import *
from flask import render_template,redirect,request,url_for,Blueprint,flash,current_app
from werkzeug.utils import secure_filename
import random
import os


blog = Blueprint(
    'blog',
    __name__,
    url_prefix='/blog',
    static_folder='static',
    template_folder='templates')

@app.route('/',methods=['GET','POST'])
def homePage():
    seo=Seo.query.all()
    blog=Blogs.query.filter_by(blogStatus=True).all()
    contact= Contact.query.all()
    about=About.query.all()
    client=Client.query.all()
    social=Social.query.all()
    portfolio=Portfolio.query.all()
    category=Category.query.all()
    if request.method == 'POST':
        form = Form(userName=request.form['name'],userEmail=request.form['email'],
            userSubject=request.form['subject'],userMessage=request.form['comments'])
        db.session.add(form)
        db.session.commit()
        return redirect ('/')
    return render_template('app/index.html',seo=seo,blog=blog,contact=contact,about=about,client=client,social=social,portfolio=portfolio,category=category)



@blog.route('/<int:id>',methods=['GET','POST'])
def blogPage(id):
    seo=Seo.query.all()
    social=Social.query.all()
    blog = Blogs.query.get(id)
    return render_template('app/blog.html',blog=blog,seo=seo,social=social)

