from datetime import datetime,date
from app import db


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50))
    userEmail = db.Column(db.String(50))
    userSubject = db.Column(db.String(100))
    userMessage = db.Column(db.Text)
    userDate = db.Column(db.DateTime,default=datetime.now())

class Blogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blogTitle = db.Column(db.String)
    blogDetail = db.Column(db.Text)
    blogAuthor = db.Column(db.String)
    blogDate = db.Column(db.Date,default=date.today())
    blogImage = db.Column(db.String)
    blogStatus = db.Column(db.Boolean)
