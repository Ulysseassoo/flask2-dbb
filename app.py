from flask import Flask, request, jsonify
from flask import render_template
import markdown
import shortuuid
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.run(debug=True)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+mysqlconnector://{user}:{password}@{server}/{database}".format(
    user="root", password="", server="localhost", database="data"
)

db = SQLAlchemy(app)


class myDB(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)


@app.route("/admin/", methods=["GET", "POST"])
def getAllData():
    datas = myDB.query.all()
    if request.method == "POST":
        if request.form["btn"] == "create":
            data = request.json
            url = shortuuid.uuid()
            newData = myDB(url=url, content=request.form["content"])
            db.session.add(newData)
            db.session.commit()
        if request.form["btn"] == "delete":
            data = myDB.query.filter_by(id=request.form["id"]).first()
            db.session.delete(data)
            db.session.commit()
            datas = myDB.query.all()
            return render_template("admin.html", test=datas, html=html)
    return render_template("admin.html", test=datas)


@app.route("/admin/<url>", methods=["GET", "POST"])
def adminData(url):
    admin = myDB.query.filter_by(url=url).first()
    if request.method == "POST":
        if request.form["btn"] == "update":
            data = myDB.query.filter_by(url=url).first()
            data.content = request.form["content"]
            db.session.commit()
            success = "You just modified this content !!"
            return render_template("modify.html", test=admin, success=success)
    return render_template("modify.html", test=admin)


@app.route("/articles/<url>")
def getData(url):
    example = myDB.query.filter_by(url=url)
    for data in example:
        paste = markdown.markdown(data.content)
    return render_template("content.html", test=example, paste=paste)


@app.route("/articles/create", methods=["GET", "POST"])
def insertData():
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
        data = request.json
        url = shortuuid.uuid()
        newData = myDB(url=url, content=request.form["content"])
        html = markdown.markdown(request.form["content"])
        db.session.add(newData)
        db.session.commit()
        return render_template("form.html", url=url, paste=html)


# def test_markdown():