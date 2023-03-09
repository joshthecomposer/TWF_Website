from flask import jsonify, send_from_directory, render_template, session, redirect, request
from flask_app import application as app
from flask_app.models.admin import Admin
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/admin/reg", methods=["GET"])
def login_reg():
    return render_template("admin_reg.html")

@app.route("/admin", methods=["GET"])
def admin_index():
    if (not Admin.check()):
        return redirect("/")
    return redirect("/admin/dashboard")

@app.route("/admin/blogs", methods=["GET"])
def blog():
    session['admin'] = 1
    if (not Admin.check()):
        return redirect("/")
    return render_template("blog.html")

@app.route("/admin/dashboard", methods=["GET"])
def dashboard():
    if (not Admin.check()):
        return redirect("/")
    return render_template("dashboard.html")

@app.route("/admin/blogs/all", methods=["GET"])
def all_blogs():
    if (not Admin.check()):
        return redirect("/")
    return render_template("all_blogs.html")

@app.route("/admin/blogs/create", methods=["POST"])
def create_blog():
    if(not Admin.check()):
        return redirect("/")
    # do things
    return redirect("/admin/blogs/all")

@app.route("/admin/tokens/generate")
def generate_token():
    if(not Admin.check()):
        return redirect("/")
    return render_template("token_form.html")