import os
from pathlib import Path


class Config:
    # Обязательные настройки БД
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'postgresql://sasha:Sasha228@localhost:5532/mydb'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Дополнительные настройки
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    UPLOAD_FOLDER = Path(__file__).parent.parent / 'static' / 'uploads'

    #SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    #SQLALCHEMY_TRACK_MODIFICATIONS = False

    SCIENCE_IMAGES = [
        "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=500",
        "https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=500",
        "https://images.unsplash.com/photo-1581094271901-8022df4466f9?w=500",
        "https://images.unsplash.com/photo-1615874694520-8229c5c8e5e2?w=500"
    ]