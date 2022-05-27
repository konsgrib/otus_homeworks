from flask import Flask, request
from views.articles import articles_app


app = Flask(__name__)

app.config.update(
    ENV="development",
    SECRET_KEY="safdtrryrthrbvcnghjk9iotfgjuy678hygbs",
)

app.register_blueprint(articles_app, url_prefix="/articles")


@app.route("/", methods=["GET", "POST"])
def hello_world():
    return {"message": "Hello, world!", "method": request.method}


@app.get("/hello/")
def handle_hello():
    name = request.args.get("name", "OTUS")
    return {"name": name}


@app.get("/hello/<name>/")
def hello_name(name):
    return {"smg": f"hello {name}"}


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
