from flask_migrate import current
from app import *

admin = Blueprint('admin',
__name__,
url_prefix='/admin',
static_folder='static',
template_folder='templates')


@admin.route('/',methods=['GET','POST'])
def adminPage():
    if not current_user.is_authenticated:
        return redirect('/auth')
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
    if not current_user.is_authenticated:
        return redirect('/auth')
    seo=Seo.query.all()
    if Seo.query.get(1):
        bos=True
    else:
        bos=False
    if request.method=='POST':
        rand=random.randint(1, 90000)
        rand1=random.randint(1, 90000)
        f = request.files['file']
        newName=f"icon{rand}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}" 
        h = request.files['homefile']
        homenewName=f"home{rand1}.{f.filename.split('.')[-1]}"
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
    if not current_user.is_authenticated:
        return redirect('/auth')
    clnt=Client.query.all()
    if request.method=='POST':
        randN=random.randint(1, 90000)
        f = request.files['file']
        newName=f"client{randN}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        client=Client(title=request.form['title'],detail=request.form['detail'],image=filePath)
        db.session.add(client)
        db.session.commit()
        return redirect('/admin/client')
    return render_template('admin/editClient.html',clnt=clnt)

@admin.route('/deleteclient/<int:id>')
def adminclientDelete(id):
    if not current_user.is_authenticated:
        return redirect('/auth')
    db.session.delete(Client.query.get(id))
    db.session.commit()
    return redirect('/admin/client')

@admin.route('/about',methods=['GET','POST'])
def adminAbout():
    if not current_user.is_authenticated:
        return redirect('/auth')
    if request.method=='POST':
        rand=random.randint(1, 90000)
        f = request.files['file']
        newName=f"about{rand}.{f.filename.split('.')[-1]}"
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
    if not current_user.is_authenticated:
        return redirect('/auth')
    blog=Blogs.query.all()
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['file']
        newName=f"blog{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Blogs(blogTitle=request.form['title'],blogDetail=request.form['detail'],
            blogAuthor=request.form['author'],blogImage=filePath))
        db.session.commit()
        return redirect('/admin/blog')
    return render_template('admin/editBlog.html',blog=blog)

@admin.route('/deleteform/<int:id>')
def adminDelete(id):
    if not current_user.is_authenticated:
        return redirect('/auth')
    db.session.delete(Form.query.get(id))
    db.session.commit()
    return redirect('/admin')

@admin.route('/deleteblog/<int:id>')
def blogDelete(id):
    if not current_user.is_authenticated:
        return redirect('/auth')
    blog=Blogs.query.get(id)
    os.unlink(os.getcwd() + blog.blogImage)
    db.session.delete(blog)
    db.session.commit()
    return redirect('/admin/blog')

@admin.route('/social',methods=['POST','GET'])
def adminSocial():
    if not current_user.is_authenticated:
        return redirect('/auth')
    sc=Social.query.all()
    if Social.query.get(1):
        bos=True
    else:
        bos=False
    if request.method=='POST':
        a = Social.query.filter_by(id = 1)
        a.delete()
        db.session.add(Social(pinterest=request.form['pinterest'],facebook=request.form['facebook'],
            instagram=request.form['instagram'],twitter=request.form['twitter']))
        db.session.commit()
        return redirect('/admin/social')
    return render_template('/admin/editSocial.html',sc=sc,bos=bos)

@admin.route('/category',methods=['POST','GET'])
def adminCategory():
    if not current_user.is_authenticated:
        return redirect('/auth')
    cat=Category.query.all()
    formcategory=CategoryForm()
    if request.method=='POST':
        db.session.add(Category(name=formcategory.name.data))
        db.session.commit()
        return redirect('/admin/category')
    return render_template('/admin/editCategory.html',form=formcategory,cat=cat)

@admin.route('/deletecategory/<int:id>')
def categoryDelete(id):
    if not current_user.is_authenticated:
        return redirect('/auth')
    db.session.delete(Category.query.get(id))
    db.session.commit()
    return redirect('/admin/category')

@admin.route('/portfolio',methods=['POST','GET'])
def adminPortfolio():
    if not current_user.is_authenticated:
        return redirect('/auth')
    formportfolio=PortfolioForm()
    if request.method=='POST':
        randNumber=random.randint(1, 90000)
        f = request.files['image']
        newName=f"portfolio{randNumber}.{f.filename.split('.')[-1]}"
        f.save(os.path.join(app.config['UPLOAD_PATH'],newName))   
        filePath=f"/{app.config['UPLOAD_PATH']}/{newName}"
        db.session.add(Portfolio(title=formportfolio.title.data,image=filePath,category_id=formportfolio.category.data))
        db.session.commit()
        return redirect('/admin/portfolio')
    return render_template('/admin/editPortfolio.html',form=formportfolio,port=Portfolio.query.all(),cat=Category.query.all())

@admin.route('/deleteportfolio/<int:id>')
def portfolioDelete(id):
    if not current_user.is_authenticated:
        return redirect('/auth')
    db.session.delete(Portfolio.query.get(id))
    db.session.commit()
    return redirect('/admin/portfolio')

@admin.route('/true/<int:id>')
def blogTrue(id):
    true=Blogs.query.get(id)
    true.blogStatus=True
    db.session.commit()
    return redirect('/admin/blog')

@admin.route('/false/<int:id>')
def blogFalse(id):
    false=Blogs.query.get(id)
    false.blogStatus=False
    db.session.commit()
    return redirect('/admin/blog')

@admin.route('/settings',methods=['POST','GET'])
def adminSettings():
    if not current_user.is_authenticated:
        return redirect('/auth')
    updateform=UpdateForm()
    if request.method=='POST':
        oldusername = User.query.filter_by(username=updateform.oldusername.data).first()
        oldpassword = User.query.filter_by(password=updateform.oldpassword.data).first()
        if oldusername and oldpassword:
            sil = User.query.filter_by(id = 1)
            sil.delete()
            db.session.add(User(username=updateform.username.data,password=updateform.password.data))
            db.session.commit()
            return redirect('/auth')
    return render_template('/admin/editSettings.html',updateform=updateform)