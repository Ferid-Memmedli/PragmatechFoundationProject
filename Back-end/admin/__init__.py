from app import app
from .routes import admin

app.register_blueprint(admin)