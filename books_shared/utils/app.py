from flask import Flask

from books_shared.utils import logger
from books_shared.utils.db import db
app = Flask(__name__)


def create_app():
    logger.info(f"Create new app")
    #app.config.from_envvar(config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
