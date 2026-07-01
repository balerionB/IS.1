# Import application factory.
from flask import render_template, Flask, Config
from flask_limiter.util import get_remote_address

from app import create_app
from app.extensions import db

# Create Flask application instance.
app = create_app()

@app.route("/")
def home():
    return render_template("landing/index.html")
# Run application only if this file is executed directly.
if __name__ == "__main__":

    # Start development server.
    app.run(debug=True)


from back_end.app.analytics.routes import analytics

app.register_blueprint(
    analytics,
    url_prefix="/analytics"
)
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)
from flask_limiter import Limiter

limiter = Limiter(

    key_func=get_remote_address,

    app=app

)
from flask_talisman import Talisman

Talisman(app)
@app.errorhandler(403)
def forbidden(error):

    return render_template(
        "errors/403.html"
    ),403


@app.errorhandler(404)
def not_found(error):

    return render_template(
        "errors/404.html"
    ),404


@app.errorhandler(500)
def server_error(error):

    db.session.rollback()

    return render_template(
        "errors/500.html"
    ),500

app = Flask(__name__)

app.config.from_object(Config)