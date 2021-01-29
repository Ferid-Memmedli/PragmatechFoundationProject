from app import *


admin = Blueprint('admin',
__name__,
url_prefix='/admin',
static_folder='static',
template_folder='templates')

@admin.route('/')
def adminPage():
    return render_template('admin/index.html')

@admin.route('/seo')
def adminSeo():
    return render_template('admin/editSeo.html')