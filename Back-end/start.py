from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/crud.db'
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(110), unique=True, nullable=False)
    code = db.Column(db.String(110))


@app.route('/',methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/blog',methods=['GET','POST'])
def blog():
    return render_template("blog.html")

@app.route('/admin',methods=['GET','POST'])
def admin():
    if request.method=='POST':
        user = User(username=request.form['username'],email=request.form['email'],code=request.form['code'])
        db.session.add(user)
        db.session.commit()
        return redirect('/admin')
    users=User.query.all()
    return render_template("admin/admin.html",userList=users)

@app.route('/delete/<int:id>')
def delete(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin')

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    user=User.query.get(id)
    if request.method=='POST':
        user.username=request.form['username']
        user.email=request.form['email']
        db.session.merge(user)
        db.session.flush()
        db.session.commit()
        return redirect('/admin')
    else:
        return render_template('admin/update.html',user=user)

if __name__ == '__main__':
    app.run(debug=True)
    manager.run()