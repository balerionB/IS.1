from app import create_app, db  # Adjust 'app' to your package name

app = create_app()

with app.app_context():
    db.create_all()  # Create tables here safely

@app.route("/")
def home():
    return {
        "message": "Server is running"
    }
if __name__ == "__main__":
    app.run(debug=True)   