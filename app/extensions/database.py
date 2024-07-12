from playhouse.flask_utils import FlaskDB

db = FlaskDB()


def configure(app):
    db.init_app(app)


def create_tables(models):
    with db.database as database:
        database.create_tables(models)
