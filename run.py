from app import create_app
from app.extensions import db
from app.blueprints.user.models import User

if __name__ == '__main__':
    flask_app = create_app('prod')
    with flask_app.app_context():
        db.create_all()

    flask_app.run()


    

