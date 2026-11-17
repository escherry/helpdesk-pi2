import os
from flask import Flask
from . import models
from .controllers import bp

def create_app(database=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-troque-em-producao")
    app.config["DATABASE"] = database or os.path.join(app.root_path, "..", "helpdesk.db")
    app.register_blueprint(bp)
    with app.app_context():
        models.init_db()
    return app
