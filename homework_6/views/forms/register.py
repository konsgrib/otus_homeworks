from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    login = StringField(
        label="Login",
        name="login",
        validators=[DataRequired(), Length(min=3)],
    )
    password = PasswordField(
        label="Password",
        name="password",
        validators=[DataRequired(), Length(min=5)],
    )
    password_2 = PasswordField(
        label="Verify password",
        name="password_2",
        validators=[DataRequired(), Length(min=5)],
    )
