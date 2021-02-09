from app import *

auth=Blueprint(
    'auth',
     __name__,
     url_prefix='/auth',
     template_folder='templates',
     static_folder='static')

@auth.route('/',methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/admin')
    login=LoginForm()
    if login.validate_on_submit():
        user = User.query.filter_by(username=login.username.data).first()
        if user and user.password == login.password.data:
            login_user(user)
            return redirect('/admin')
        else:
            flash(f'Wrong Username or Password','success')
    return render_template('auth/login.html',login=login)

@auth.route('/logout',methods=['POST','GET'])
def logout():
    logout_user()
    return redirect('/auth')
