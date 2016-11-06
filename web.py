from flask import Flask, render_template
from sqlalchemy import create_engine
from config import DATABASE_FILE_NAME


webApp = Flask("", template_folder='templates', static_folder='static')

if DATABASE_FILE_NAME.startswith("sqlite:///"):
    db = create_engine(DATABASE_FILE_NAME)
else:
    db = create_engine("sqlite:///%s" % DATABASE_FILE_NAME)

@webApp.route("/")
def index():
    return render_template("index.html"), 200
