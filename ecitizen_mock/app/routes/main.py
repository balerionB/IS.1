from flask import Blueprint, render_template

# Create the blueprint and name it 'main' (or whatever you prefer)
# This creates the 'bp' object that app.py is looking for
bp = Blueprint('main', __name__)


@bp.route('/')
def home():
    # Make sure this path matches your folder structure
    # If you kept files in 'public', use:
    return render_template("index.html")

    # If you moved files to 'templates', use:
    # return render_template("index.html")