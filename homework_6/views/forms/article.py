from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField
from wtforms.validators import DataRequired, Length


class ArticleForm(FlaskForm):
    article_text = TextAreaField(
        label="Text",
        name="article_text",
        validators=[DataRequired(), Length(min=5)],
    )
    article_title = StringField(
        label="Title",
        name="article_title",
        validators=[DataRequired(), Length(min=5)],
    )
    article_user_id = HiddenField(
        name="article_user_id",
        validators=[DataRequired()],
    )
