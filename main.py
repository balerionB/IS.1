from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:qwerty12345@127.0.0.1:5432/ps_srms', echo=False)
from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def home():

    return render_template("public/index.html")