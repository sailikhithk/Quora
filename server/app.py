from routes.routes import create_app

app, db = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # This will create the database tables based on the model definitions
    app.run(debug=True)
