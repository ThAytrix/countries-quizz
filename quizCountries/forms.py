from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from quizCountries.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Nom d\'utilisateur',
                           validators=[DataRequired(message="Veuillez renseigner un pseudo"), Length(min=2, max=20, message="Votre pseudo doit être compris entre 2 et 20 caractères")])
    email = StringField('Email',
                        validators=[DataRequired(message="Veuillez renseigner un mail"), Email(message="Veuillez renseigner un mail valide")])
    password = PasswordField('Mot de passe', validators=[DataRequired(message="Veuillez renseigner un mot de passe")])
    confirm_password = PasswordField('Confirmer le mot de passe',
                                     validators=[DataRequired(message="Veuillez renseigner un mot de passe"), EqualTo('password', message="Les deux mots de passe ne sont pas identiques")])
    submit = SubmitField('S\'inscrire')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Ce nom d\'utilisateur est pris. Veuillez en choisir un autre.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Cette adresse électronique est prise. Veuillez en choisir une autre.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message="Veuillez renseigner votre mail"), Email(message="Veuillez renseigner un mail valide")])
    password = PasswordField('Mot de passe', validators=[DataRequired(message="Veuillez renseigner votre mot de passe")])
    remember = BooleanField('Se souvenir de moi')
    submit = SubmitField('Se connecter')
