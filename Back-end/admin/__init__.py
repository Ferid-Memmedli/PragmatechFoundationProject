from app import app
from admin.routes import admin

app.register_blueprint(admin)