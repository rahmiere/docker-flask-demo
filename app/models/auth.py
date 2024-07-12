from peewee import CharField

from app.extensions import db


class User(db.Model):
    username = CharField(unique=True)
