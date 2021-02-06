from app import app
from .routes import auth

app.register_blueprint(auth)