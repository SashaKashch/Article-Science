#инициализация расширений для фласк



from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#import flask_bcrypt
#from flask_bcrypt import Bcrypt


db = SQLAlchemy()
migrate = Migrate()
#bcrypt = flask_bcrypt.Bcrypt()
