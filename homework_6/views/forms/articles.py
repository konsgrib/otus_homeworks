from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ArticleForm(FlaskForm):
    article_text = StringField(
        label="New Article",
        name="article_text" "article-text",
        validators=[DataRequired(), Length(min=5)],
    )
