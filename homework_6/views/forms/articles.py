from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ArticleForm(FlaskForm):
    article_text = StringField(
        label="New Article",
        name="article_text" "article-text",
        validators=[DataRequired(), Length(min=5)],
    )
    article_title = StringField(
        label="New Article Title",
        name="article_title" "article-title",
        validators=[DataRequired(), Length(min=5)],
    )
    article_author_id = StringField(
        label="Author id",
        name="article_author_id" "article-author-id",
        validators=[DataRequired(), Length(min=1)],
    )
