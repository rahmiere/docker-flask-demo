from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

from app import models  

admin = Admin(name="Admin Panel")


class UserView(ModelView):
    column_exclude_list = ("id",)


admin.add_view(UserView(models.User))


def configure(app):
    admin.init_app(app)
