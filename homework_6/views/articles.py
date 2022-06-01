import logging
from flask import Blueprint, jsonify, render_template, request, url_for, redirect
from psycopg2 import IntegrityError
from werkzeug.exceptions import NotFound, BadRequest
from models.user import User
from models.articles import Article
from models import db
from views.forms.article import ArticleForm
from flask_login import login_user, login_required

log = logging.getLogger(__name__)
articles_app = Blueprint("articles_app", __name__)


@articles_app.get("/", endpoint="list")
def list_articles():
    users: list[User] = User.query.all()
    user_id = request.args.get("user_id")
    if not user_id:
        articles: list[Article] = Article.query.all()
    else:
        articles: list[Article] = Article.query.filter_by(user_id=user_id)
    return render_template("articles/list.html", articles=articles, users=users)


@articles_app.get("/<int:article_id>/", endpoint="details")
def get_article(article_id):
    article: Article = Article.query.get_or_404(article_id)
    return render_template("articles/details.html", article=article)


@articles_app.get("/<int:author_id>/")
def get_author_by_id(author_id):
    return {
        "author": author_id,
    }


@articles_app.route("/add/", methods=["GET", "POST"], endpoint="add")
@login_required
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
    article_user_id = form.data["article_user_id"]

    article = Article(
        user_id=article_user_id,
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
