from flask import jsonify, send_from_directory, render_template, session, redirect, request, flash
from flask_app import application as app
from flask_app.models.admin import Admin
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/admin/reg", methods=["GET"])
def login_reg():
    return render_template("login_reg.html")

@app.route("/admin", methods=["GET"])
def admin_index():
    if (not Admin.session_check()):
        return redirect("/")
    return redirect("/admin/dashboard")

@app.route("/admin/blogs", methods=["GET"])
def blog():
    if (not Admin.session_check()):
        return redirect("/")
    return render_template("blog.html")

@app.route("/admin/dashboard", methods=["GET"])
def dashboard():
    if (not Admin.session_check()):
        return redirect("/")
    return render_template("dashboard.html")

@app.route("/admin/blogs/all", methods=["GET"])
def all_blogs():
    if (not Admin.session_check()):
        return redirect("/")
    return render_template("all_blogs.html")

@app.route("/admin/blogs/create", methods=["POST"])
def create_blog():
    if(not Admin.session_check()):
        return redirect("/")
    # do things
    return redirect("/admin/blogs/all")

@app.route("/admin/tokens/generate")
def generate_token():
    if(not Admin.session_check()):
        return redirect("/")
    return render_template("token_form.html")

@app.route("/admin/create", methods=["POST"])
def create():
    data = {
        "token" : request.form["token"]
    }
    if (not Admin.validate_admin_token(data)):
        flash("Invalid token")
        return redirect("/admin/reg")
    data  = {
        "email" : request.form["email"]
    }
    if (Admin.email_exists(data)):
        flash("Email already exists")
        return redirect("/admin/reg")
    if (Admin.validate(request.form)):
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        data = {
            "first_name":request.form["first_name"],
            "last_name":request.form["last_name"],
            "email":request.form["email"],
            "password":pw_hash
        }
        Admin.create(data)
    return redirect("/admin/dashboard")

@app.route("/admin/logout")
def logout():
    session.clear()
    return redirect("/")