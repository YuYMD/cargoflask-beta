from flask_mail import Mail
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt


mail = Mail()
csrf = CSRFProtect()
db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()
bcrypt = Bcrypt()

