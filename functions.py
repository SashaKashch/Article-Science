#вспомогательные функции
import secrets
import os.path

#import image
from flask import current_app

def save_picture(picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.config['SERVER_PAT'], picture_fn)
    output_size = (125, 125)
    #i = image.open(picture)
   # i.thumbnail(output_size)
    #i.save(picture_path)
    return picture_fn