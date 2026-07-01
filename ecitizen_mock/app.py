from app import create_app
from flask import Flask
app = create_app()

app = Flask(__name__, template_folder='public')

# Your existing routes and code go here...
# If you imported routes, they stay the same
from app.routes import main
app.register_blueprint(main.bp) 

if __name__ == '__main__':
    app.run(debug=True)