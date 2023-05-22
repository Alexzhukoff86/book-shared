from flask import Flask

from db import db
app = Flask(__name__)

# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///account.db'


def create_app(config):
    app.config.from_envvar(config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
