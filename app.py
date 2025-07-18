from website import create_app
from models import db

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

with app.app_context():
    db.create_all()
    print("Database and tables created successfully!")