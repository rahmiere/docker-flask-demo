from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from .config import Config

    app.config.from_object(Config)

    # register extensions
    from .extensions import admin, database

    admin.configure(app)
    database.configure(app)

    # import all models and create the tables
    from .models import models

    database.create_tables(models)

    # register routes
    from .routes import blueprint as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
