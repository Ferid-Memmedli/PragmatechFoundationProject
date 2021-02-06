from datetime import datetime,date
from app import db


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50),nullable=False)
    userEmail = db.Column(db.String(50),nullable=False)
    userSubject = db.Column(db.String(100),nullable=False)
    userMessage = db.Column(db.Text,nullable=False)
    userDate = db.Column(db.DateTime,default=datetime.now())

class Blogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blogTitle = db.Column(db.String,nullable=False)
    blogDetail = db.Column(db.Text,nullable=False)
    blogAuthor = db.Column(db.String,nullable=False)
    blogDate = db.Column(db.String,default=datetime.now().strftime('%d %B %Y'))
    blogImage = db.Column(db.String,nullable=False)
    blogStatus = db.Column(db.Boolean)
    def __init__(self,blogTitle,blogDetail,blogAuthor,blogImage):
        self.blogDetail=blogDetail
        self.blogAuthor=blogAuthor
        self.blogImage=blogImage
        self.blogTitle=blogTitle
        self.blogStatus = True

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    elaqe = db.Column(db.String(100),nullable=False)
    unvan = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False)

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20),nullable=False)
    detail = db.Column(db.Text,nullable=False)
    image = db.Column(db.String,nullable=False)

class Seo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20),nullable=False)
    keywords = db.Column(db.String(20),nullable=False)
    image = db.Column(db.String,nullable=False)
    homeimage = db.Column(db.String,nullable=False)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20),nullable=False)
    detail = db.Column(db.String,nullable=False)
    image = db.Column(db.String,nullable=False)

class Social(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pinterest = db.Column(db.String)
    facebook = db.Column(db.String)
    instagram = db.Column(db.String)
    twitter = db.Column(db.String)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable=False)
    port = db.relationship('Portfolio',backref='category',lazy=True)

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String,nullable=False)
    image = db.Column(db.String,nullable=False)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'),nullable=False)

