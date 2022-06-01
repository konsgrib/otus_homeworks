from os import getenv
from flask import Flask, render_template, request, current_app
from views.articles import articles_app
from flask_sqlalchemy import SQLAlchemy
from models import db, Article
from flask_migrate import Migrate

app = Flask(__name__)

CONFIG_NAME = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_NAME}")


app.register_blueprint(articles_app, url_prefix="/articles")
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/", endpoint="list")
def list_products():
    articles: list[Article] = Article.query.all()
    return render_template("articles/list.html", articles=articles)


@app.get("/authors/<int:author_id>/")
def get_author_by_id(author_id):
    return {
        "author": author_id,
    }


@app.get("/authors/<int:author_id>/books/<int:book_id>")
def get_author_books_by_ids(author_id, book_id):
    return {
        "author": author_id,
        "book_id": book_id,
    }


if __name__ == "__main__":
    app.run(debug=True)
