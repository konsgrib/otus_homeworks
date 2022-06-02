from os import getenv
from urllib import response
from flask import Flask, redirect, render_template, request, current_app, flash, url_for
from views.articles import articles_app
from flask_sqlalchemy import SQLAlchemy
from models import db, Article, User
from flask_migrate import Migrate
from flask_login import LoginManager, logout_user

# for user
from views.forms.login import LoginForm
from views.forms.register import RegisterForm
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required

# for user
app = Flask(__name__)

CONFIG_NAME = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_NAME}")


app.register_blueprint(articles_app, url_prefix="/articles")
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()  # for user
login_manager.init_app(app)


@app.route("/", endpoint="list")
# @login_required
def list_products():
    users: list[User] = User.query.all()
    articles: list[Article] = Article.query.all()
    return render_template("articles/list.html", articles=articles, users=users)


@app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    form = LoginForm()
    login = form.data["login"]
    password = form.data["password"]
    if login and password:
        user = User.query.filter_by(login=login).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect("/")
        else:
            flash("Login failed")
    return render_template("user/login.html", form=form)


@app.route("/register/", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    login_form = LoginForm()
    login = request.form.get("login")
    password = request.form.get("password")
    password2 = request.form.get("password_2")

    if request.method == "POST":
        if not (login or password or password2):
            flash("Please fill all fields")
        elif password != password2:
            flash("Password does not match")
        else:
            hashed_password = generate_password_hash(password)
            new_user = User(login=login, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for("login"))
    return render_template("user/register.html", form=form)


@app.route("/logout/", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect("/login?next=" + request.path)


if __name__ == "__main__":
    app.run(debug=True)
