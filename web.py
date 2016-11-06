from flask import Flask, render_template
from config import DATABASE_FILE_NAME


webApp = Flask("", template_folder='templates', static_folder='static')

@webApp.route("/")
def index():
    return render_template("index.html"), 200
