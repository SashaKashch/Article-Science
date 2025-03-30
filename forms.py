#формы wtf для регистрации и других действий

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

from .models.user import User

class RegistrationForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired(), Length(min=2, max=30)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')

    name = StringField('ФИО', validators=[DataRequired(), Length(min=2, max=30)])
    avatar = FileField('Мое изображение', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    group = StringField('Моя группа')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Данное имя уже занято')