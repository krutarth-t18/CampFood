from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'campfood'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/campfood_webapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager(app)
# login_manager.init_app(app)
# login_manager.login_view = "signin"


@login_manager.user_loader
def load_user(Sno):
    from CampFood.models import Registration
    return Registration.query.get(int(Sno))


from CampFood import routes
