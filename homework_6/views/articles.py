from flask import Blueprint, jsonify, render_template, request, url_for, redirect
from werkzeug.exceptions import NotFound, BadRequest

from views.forms.articles import ArticleForm

articles_app = Blueprint("articles_app", __name__)


ARTICLES = {
    1: {
        "author": "Bill",
        "title": "The first Article",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean commodo massa nec tortor consectetur sollicitudin. Aliquam id ipsum consectetur, cursus justo vitae, imperdiet mauris. Nullam id ornare turpis. Duis pretium velit nec velit sagittis vulputate. In interdum feugiat tempor. Cras euismod sapien tortor, ac porttitor tellus elementum quis. Mauris et quam nec arcu ultrices iaculis. Integer id tincidunt purus, at semper lorem. Maecenas blandit diam et fringilla interdum. Aliquam non mattis purus. Curabitur et ornare velit. Etiam placerat eu eros ac maximus. Sed semper magna lectus, vel auctor diam malesuada nec. Integer faucibus viverra lacus ac accumsan. Maecenas elementum libero ac fringilla ullamcorper. Maecenas cursus ante in ligula sollicitudin pharetra. Etiam non imperdiet tellus. Nulla pretium tempor ipsum, et porta nibh luctus at. Praesent bibendum faucibus ante nec viverra. ",
    },
    2: {
        "author": "John",
        "title": "The second Article",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean commodo massa nec tortor consectetur sollicitudin. Aliquam id ipsum consectetur, cursus justo vitae, imperdiet mauris. Nullam id ornare turpis. Duis pretium velit nec velit sagittis vulputate. In interdum feugiat tempor. Cras euismod sapien tortor, ac porttitor tellus elementum quis. Mauris et quam nec arcu ultrices iaculis. Integer id tincidunt purus, at semper lorem. Maecenas blandit diam et fringilla interdum. Aliquam non mattis purus. Curabitur et ornare velit. Etiam placerat eu eros ac maximus. Sed semper magna lectus, vel auctor diam malesuada nec. Integer faucibus viverra lacus ac accumsan. Maecenas elementum libero ac fringilla ullamcorper. Maecenas cursus ante in ligula sollicitudin pharetra. Etiam non imperdiet tellus. Nulla pretium tempor ipsum, et porta nibh luctus at. Praesent bibendum faucibus ante nec viverra. ",
    },
    3: {
        "author": "Alex",
        "title": "The third Article",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean commodo massa nec tortor consectetur sollicitudin. Aliquam id ipsum consectetur, cursus justo vitae, imperdiet mauris. Nullam id ornare turpis. Duis pretium velit nec velit sagittis vulputate. In interdum feugiat tempor. Cras euismod sapien tortor, ac porttitor tellus elementum quis. Mauris et quam nec arcu ultrices iaculis. Integer id tincidunt purus, at semper lorem. Maecenas blandit diam et fringilla interdum. Aliquam non mattis purus. Curabitur et ornare velit. Etiam placerat eu eros ac maximus. Sed semper magna lectus, vel auctor diam malesuada nec. Integer faucibus viverra lacus ac accumsan. Maecenas elementum libero ac fringilla ullamcorper. Maecenas cursus ante in ligula sollicitudin pharetra. Etiam non imperdiet tellus. Nulla pretium tempor ipsum, et porta nibh luctus at. Praesent bibendum faucibus ante nec viverra. ",
    },
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
        articles=ARTICLES.items(),
    )


@articles_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_article():
    form = ArticleForm()

    if request.method == "GET":
        return (
            render_template(
                "articles/add.html",
                form=form,
                articles=ARTICLES.items(),
            ),
            400,
        )

    if not form.validate_on_submit():
        return render_template("articles/add.html", form=form)
    article_text = form.data["article_text"]
    article_title = form.data["article_title"]
    article_author_id = form.data["article_author_id"]

    article_id = len(ARTICLES) + 1
    ARTICLES[article_id] = {
        "title": article_title,
        "text": article_text,
        "author": article_author_id,
    }

    url_article = url_for("articles_app.details", article_id=article_id)
    return redirect(url_article)
