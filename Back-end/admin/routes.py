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
    seo=Seo.query.all()
    if Seo.query.get(1):
        bos=True
    else:
        bos=False
    if request.method=='POST':
        rand=random.randint(1, 90000)
        rand1=random.randint(1, 90000)
        f = request.files['file']
        newName=f"blogfile{rand}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}" 
        h = request.files['homefile']
        homenewName=f"blogfile{rand1}.{f.filename.split('.')[-1]}"
        h.save(os.path.join(app.config['UPLOAD_PATH'],homenewName))
        homefilePath=f"/{app.config['UPLOAD_PATH']}/{homenewName}" 
        about = Seo.query.filter_by(id = 1)
        about.delete()
        seo=Seo(title=request.form['title'],keywords=request.form['keywords'],image=filePath,homeimage=homefilePath)
        db.session.add(seo)
        db.session.commit()
        return redirect('/admin/seo')
    return render_template('admin/editSeo.html',seo=seo,bos=bos)

@admin.route('/client',methods=['GET','POST'])
def adminClient():
    clnt=Client.query.all()
    if request.method=='POST':
        randN=random.randint(1, 90000)
        f = request.files['file']
        newName=f"blogfile{randN}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        client=Client(title=request.form['title'],detail=request.form['detail'],image=filePath)
        db.session.add(client)
        db.session.commit()
        return redirect('/admin/client')
    return render_template('admin/editClient.html',clnt=clnt)

@admin.route('/deleteclient/<int:id>')
def adminclientDelete(id):
    clnt=Client.query.get(id)
    db.session.delete(clnt)
    db.session.commit()
    return redirect('/admin/client')

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

@admin.route('/social',methods=['POST','GET'])
def adminSocial():
    sc=Social.query.all()
    if Social.query.get(1):
        bos=True
    else:
        bos=False
    if request.method=='POST':
        a = Social.query.filter_by(id = 1)
        a.delete()
        social=Social(pinterest=request.form['pinterest'],facebook=request.form['facebook'],
            instagram=request.form['instagram'],twitter=request.form['twitter'])
        db.session.add(social)
        db.session.commit()
        return redirect('/admin/social')
    return render_template('/admin/editSocial.html',sc=sc,bos=bos)

@admin.route('/deletesocial/<int:id>')
def socialDelete(id):
    sc=Social.query.get(id)
    db.session.delete(sc)
    db.session.commit()
    return redirect('/admin/social')