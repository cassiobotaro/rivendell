import os

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("hello.html")


@app.route("/files/<path:filename>")
def download_files(filename):
    files = os.path.join(app.root_path, "files")
    return send_from_directory(
        directory=files, filename=filename, as_attachment=True
    )


@app.route("/files")
def list_files():
    files = os.listdir(os.path.join(app.root_path, "files"))
    return render_template("list_files.html", files=files)
