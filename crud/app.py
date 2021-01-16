from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/data.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

@app.route("/",methods=['GET','POST'])
def home():
    return render_template("index.html")

@app.route("/add")
def add():
    db.session.add(User(username="rrkkkwe", email="asdhares@jnjexample.com"))
    db.session.commit()
    users = User.query.all()
    return render_template("add.html",userList=users)

if __name__ == "__main__":
    app.run(debug=True)
