from flask import Blueprint, render_template

home = Blueprint('home',__name__,template_folder="views",static_folder='public')


@home.route('/',methods = ["GET"])
def homeIndex():
    return render_template('index.html')


@home.route('/shortcode',methods = ["GET"])
def shortcode():
    return render_template("about.html")