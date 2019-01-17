import os

from flask import Flask, send_from_directory, render_template_string

app = Flask(__name__)


@app.route("/files/<path:filename>")
def download_files(filename):
    files = os.path.join(app.root_path, "files")
    return send_from_directory(
        directory=files, filename=filename, as_attachment=True
    )


LIST_TEMPLATE_STRING = """
{% for file in  files %}
<a href="{{ url_for('download_files', filename=file) }}">{{file}}</a>
{% endfor %}
"""


@app.route("/files")
def list_files():
    files = os.listdir(os.path.join(app.root_path, "files"))
    return render_template_string(LIST_TEMPLATE_STRING, files=files)
