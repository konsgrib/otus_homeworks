from flask import Blueprint, jsonify, render_template, request, url_for, redirect
from werkzeug.exceptions import NotFound, BadRequest

from views.forms.articles import ArticleForm

articles_app = Blueprint("articles_app", __name__)


ARTICLES = {
    1: {"title": "one", "text": "sdfafadsfdsfasdfsfsafsd"},
    2: {"title": "two", "text": "134134324423432"},
    3: {"title": "three", "text": "sdfafadsfds4565465345sdfsfsafsd"},
}


@articles_app.get("/", endpoint="list")
def list_articles():
    return render_template("articles/list.html", articles=ARTICLES.items())


@articles_app.get("/<int:article_id>/", endpoint="details")
def get_article(article_id):
    article_text = ARTICLES.get(article_id)
    if article_text is None:
        raise NotFound(f"Article with is {article_id} not found!")
    return render_template(
        "articles/details.html",
        article_id=article_id,
        article_text=article_text,
    )


@articles_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_article():
    form = ArticleForm()

    if request.method == "GET":
        return render_template("articles/add.html", form=form), 400

    if not form.validate_on_submit():
        return render_template("articles/add.html", form=form)
    article_text = form.data["article_text"]

    article_id = len(ARTICLES) + 1
    ARTICLES[article_id] = article_text

    url_article = url_for("articles_app.details", article_id=article_id)
    return redirect(url_article)
