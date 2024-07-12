from flask import Blueprint, render_template

blueprint = Blueprint("core", __name__)


@blueprint.route("/")
def home():
    return render_template("index.html")
