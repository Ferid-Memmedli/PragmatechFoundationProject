from flask import Flask,render_template,request,redirect,url_for
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import StringField,SubmitField,IntegerField,SelectField,TextAreaField
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from datetime import datetime,date
import random
import os
app=Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
app.config['UPLOAD_PATH'] ='static/upload'
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class RegForm(FlaskForm):
    name=StringField('Your Name')
    surname=StringField('Your Surname')
    submit=SubmitField()

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


@app.route('/',methods=['GET','POST'])
def index():
    blog=Blogs.query.all()
    return render_template("index.html",blogs=blog)



@app.route('/blog/<int:id>',methods=['GET','POST'])
def blog(id):
    blog=Blogs.query.get(id)
    return render_template("blog.html",blogs=blog)


# --------------------------------------Admin Panel-----------------------------------------------------------
@app.route('/blog/add',methods=['GET','POST'])
def blogadd():
    if request.method == 'POST':
        randNumber=random.randint(1, 9000);
        f = request.files['image']
        newName=f"blogfile{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'] , secure_filename(newName)))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        blog = Blogs(blogTitle=request.form['title'],blogDetail=request.form['detail'],
            blogAuthor=request.form['author'],blogImage=filePath,blogStatus=True)
        db.session.add(blog)
        db.session.commit()
        return redirect('/admin')  
    return render_template("admin/admin.html")

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        form = Form(userName=request.form['name'],userEmail=request.form['email'],
            userSubject=request.form['subject'],userMessage=request.form['comments'])
        db.session.add(form)
        db.session.commit()
        return redirect('/')
    return render_template("index.html")

@app.route('/admin',methods=['GET','POST'])
def admin():
    regform=RegForm()
    form=Form.query.all()
    if regform.submit():
        data=regform.name.data
        return render_template("admin/admin.html",form=form,regform=regform,data=data)
    return render_template('admin/admin.html')

@app.route('/delete/<int:id>')
def delete(id):
    form=Form.query.get(id)
    db.session.delete(form)
    db.session.commit()
    return redirect('/admin')


# @app.route('/update/<int:id>',methods=['GET','POST'])
# def update(id):
#     user=User.query.get(id)
#     if request.method=='POST':
#         user.username=request.form['username']
#         user.email=request.form['email']
#         db.session.merge(user)
#         db.session.flush()
#         db.session.commit()
#         return redirect('/admin')
#     else:
#         return render_template('admin/update.html',user=user)

if __name__ == '__main__':
    app.run(debug=True)
    manager.run()