import logging
from flask import Blueprint, jsonify, render_template, request, url_for, redirect
from psycopg2 import IntegrityError
from werkzeug.exceptions import NotFound, BadRequest
from models.articles import Article
from models import db
from views.forms.article import ArticleForm


log = logging.getLogger(__name__)
articles_app = Blueprint("articles_app", __name__)


@articles_app.get("/", endpoint="list")
def list_articles():
    articles: list[Article] = Article.query.all()
    return render_template("articles/list.html", articles=articles)


@articles_app.get("/<int:article_id>/", endpoint="details")
def get_article(article_id):
    article: Article = Article.query.get_or_404(article_id)
    return render_template("articles/details.html", article=article)


@articles_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_article():
    form = ArticleForm()

    if request.method == "GET":
        return (
            render_template(
                "articles/add.html",
                form=form,
            ),
            400,
        )

    if not form.validate_on_submit():
        return render_template("articles/add.html", form=form)
    article_text = form.data["article_text"]
    article_title = form.data["article_title"]
    article_author_id = form.data["article_author_id"]

    article = Article(
        author=article_author_id,
        title=article_title,
        text=article_text,
    )

    db.session.add(article)

    try:
        db.session.commit()
    except:
        log.exception("Couldn't add article")
        db.session.rollback()
        raise BadRequest("Could not save article")

    url_article = url_for("articles_app.details", article_id=article.id)
    return redirect(url_article)
