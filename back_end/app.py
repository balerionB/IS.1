# Import application factory.
from app import create_app

# Create Flask application instance.
app = create_app()


# Run application only if this file is executed directly.
if __name__ == "__main__":

    # Start development server.
    app.run(debug=True)


from routes.analytics import analytics

app.register_blueprint(
    analytics,
    url_prefix="/analytics"
)