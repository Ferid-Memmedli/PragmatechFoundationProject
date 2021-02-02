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
    blogDate = db.Column(db.Date,default=date.today())
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

