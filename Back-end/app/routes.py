from app import app,db
from forms import *
from models import *
from flask import render_template,redirect,request,url_for,Blueprint
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
    blog=Blogs.query.all()
    contact= Contact.query.all()
    if request.method == 'POST':
        form = Form(userName=request.form['name'],userEmail=request.form['email'],
            userSubject=request.form['subject'],userMessage=request.form['comments'])
        db.session.add(form)
        db.session.commit()
        return redirect ('/')
    return render_template('app/index.html',blog=blog,contact=contact)



@blog.route('/<int:id>',methods=['GET','POST'])
def blogPage(id):
    a = Blogs.query.get(id)
    return render_template('app/blog.html',blog=a)

















# # --------------------------------------Admin Panel-----------------------------------------------------------
# @app.route('/blog/add',methods=['GET','POST'])
# def blogadd():
#     if request.method == 'POST':
#         randNumber=random.randint(1, 9000);
#         f = request.files['image']
#         newName=f"blogfile{randNumber}.{f.filename.split('.')[-1]}"
#         f.save(os.path.join(app.config['UPLOAD_PATH'] , secure_filename(newName)))   
#         filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
#         blog = Blogs(blogTitle=request.form['title'],blogDetail=request.form['detail'],
#             blogAuthor=request.form['author'],blogImage=filePath,blogStatus=True)
#         db.session.add(blog)
#         db.session.commit()
#         return redirect('/admin')  
#     return render_template("admin/admin.html")

# @app.route('/add',methods=['GET','POST'])
# def add():
#     if request.method == 'POST':
#         form = Form(userName=request.form['name'],userEmail=request.form['email'],
#             userSubject=request.form['subject'],userMessage=request.form['comments'])
#         db.session.add(form)
#         db.session.commit()
#         return redirect('/')
#     return render_template("index.html")

# @app.route('/admin',methods=['GET','POST'])
# def admin():
#     regform=RegForm()
#     form=Form.query.all()
#     if regform.submit():
#         data=regform.name.data
#         return render_template("admin/admin.html",form=form,regform=regform,data=data)
#     return render_template('admin/admin.html')

# @app.route('/delete/<int:id>')
# def delete(id):
#     form=Form.query.get(id)
#     db.session.delete(form)
#     db.session.commit()
#     return redirect('/admin')


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
