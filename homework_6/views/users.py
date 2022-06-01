from flask import Blueprint, jsonify, render_template, request, url_for, redirect
from werkzeug.exceptions import NotFound, BadRequest

from views.forms.articles import ArticleForm

authors_app = Blueprint("authors_app", __name__)


AUTHORS = {
    1: {
        "id": 1,
        "name": "John",
        "email": "john@gmail.com",
    },
    2: {
        "id": 2,
        "name": "Matt",
        "email": "matt@gmail.com",
    },
    3: {
        "id": 3,
        "name": "Jane",
        "email": "jane@gmail.com",
    },
}


@authors_app.get("/<int:author_id>/", endpoint="by_author")
def get_articles_by_author_id(author_id):
    articles_list = [s for s in AUTHORS if s["id"] == author_id]
    if len(articles_list) == 0:
        raise NotFound(f"Article with is {author_id} not found!")
    return render_template(
        "articles/list.html",
        author_id=author_id,
        articles=AUTHORS.items(),
    )
