# app/__init__.py
import os
from flask import Flask
from itsdangerous import URLSafeTimedSerializer
from app.blueprints.cargo import main
from app.blueprints.user import user
from app.blueprints.user.models import User
from app.extensions import (
    mail,
    csrf,
    db,
    login_manager,
    bootstrap,
    bcrypt
)



def create_app(config_type):  # dev, test, or prod

    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)

    app.register_blueprint(main)
    app.register_blueprint(user)
    extensions(app)
    authentication(app, User)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    mail.init_app(app)
    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)  # initialize bootstrap
    bcrypt.init_app(app)

    return None


def authentication(app, user_model):
    """
    Initialize the Flask-Login extension (mutates the app passed in).

    :param app: Flask application instance
    :param user_model: Model that contains the authentication information
    :type user_model: SQLAlchemy model
    :return: None
    """
    login_manager.login_view = 'user.login'

    @login_manager.user_loader
    def load_user(uid):
        return user_model.query.get(uid)

    @login_manager.token_loader
    def load_token(token):
        duration = app.config['REMEMBER_COOKIE_DURATION'].total_seconds()
        serializer = URLSafeTimedSerializer(app.secret_key)

        data = serializer.loads(token, max_age=duration)
        user_uid = data[0]

        return user_model.query.get(user_uid)

#    @login_manager.request_loader
#    def load_token(request):
#        duration = app.config['REMEMBER_COOKIE_DURATION'].total_seconds()
#        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
#        token = request.args.get('token')
#
#        data = serializer.loads(token, max_age=duration)
#        user_uid = data[0]
#
#        return user_model.query.get(user_uid)
