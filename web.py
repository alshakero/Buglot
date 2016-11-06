# @Author: Fadi Hanna Al-Kass (ceo@shaykeapp.com)

from flask import Flask, render_template


webApp = Flask("", template_folder='templates', static_folder='static')

@webApp.route("/")
def index():
    return render_template("index.html"), 200
