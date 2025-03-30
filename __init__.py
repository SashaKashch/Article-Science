from flask import Flask
from .config import Config
from .extensions import db, migrate
from .routes.main import main as main
from .routes.user import user as user
from .routes.events import events_bp

def create_app():
    app = Flask(__name__)
    # ...
    app.register_blueprint(events_bp)
    return app


def create_app(config_class=Config):
    app = Flask(__name__)

    # Загрузка конфигурации
    app.config.from_object(config_class)

    # Проверка наличия обязательных настроек
    required_keys = ['SQLALCHEMY_DATABASE_URI']
    for key in required_keys:
        if key not in app.config:
            raise ValueError(f"Не найдена обязательная настройка: {key}")

    # Инициализация расширений
    db.init_app(app)
    migrate.init_app(app, db)

    # Регистрация blueprint'ов
    from .routes.main import main
    from .routes.user import user
    from .routes.post import post

    app.register_blueprint(main)
    app.register_blueprint(user)
    app.register_blueprint(post)

    return app