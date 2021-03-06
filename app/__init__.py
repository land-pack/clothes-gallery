from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from log import create_logger

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    from .gallery import gallery as gallery_blueprint
    app.register_blueprint(gallery_blueprint, url_prefix='/gallery')

    # import logging
    # handler = create_logger('/var/log/gallery.log', level=logging.INFO)
    # app.logger.addHandler(handler)

    return app
