from app import *

admin = Blueprint('admin',
__name__,
url_prefix='/admin',
static_folder='static',
template_folder='templates')


@admin.route('/',methods=['GET','POST'])
def adminPage():
    form=Form.query.all()
    contact=Contact.query.all()
    if Contact.query.get(1):
        bos=True
    else:
        bos=False
    if request.method=='POST':
        contact = Contact.query.filter_by(id = 1)
        contact.delete()
        ctc=Contact(elaqe=request.form['elaqe'],unvan=request.form['unvan'],
            email=request.form['email'])
        db.session.add(ctc)
        db.session.commit()
        return redirect('/admin')
    return render_template('admin/index.html',form=form,contact=contact,bos=bos)

@admin.route('/seo',methods=['GET','POST'])
def adminSeo():
    return render_template('admin/editSeo.html')

@admin.route('/client',methods=['GET','POST'])
def adminClient():
    return render_template('admin/editClient.html')

@admin.route('/about',methods=['GET','POST'])
def adminAbout():
    if request.method=='POST':
        rand=random.randint(1, 90000)
        f = request.files['file']
        newName=f"blogfile{rand}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}" 
        about = About.query.filter_by(id = 1)
        about.delete()
        abt=About(title=request.form['title'],detail=request.form['detail'],
            image=filePath)
        db.session.add(abt)
        db.session.commit()
        return redirect('/admin/about')
    return render_template('admin/editAbout.html')

@admin.route('/blog',methods=['GET','POST'])
def adminBlog():
    blog=Blogs.query.all()
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"blogfile{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        blog=Blogs(blogTitle=request.form['title'],blogDetail=request.form['detail'],
            blogAuthor=request.form['author'],blogImage=filePath)
        db.session.add(blog)
        db.session.commit()
        return redirect('/admin/blog')
    return render_template('admin/editBlog.html',blog=blog)

@admin.route('/deleteform/<int:id>')
def adminDelete(id):
    form=Form.query.get(id)
    db.session.delete(form)
    db.session.commit()
    return redirect('/admin')

@admin.route('/deleteblog/<int:id>')
def blogDelete(id):
    blog=Blogs.query.get(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect('/admin/blog')