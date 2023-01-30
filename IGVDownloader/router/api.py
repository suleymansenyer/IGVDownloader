from flask import Blueprint
from ig import video_get_source , ig_get_pp

api = Blueprint('Blueprint',__name__)

@api.route("/pp/<username>")
def user_pp(username):
    return ig_get_pp(username)


@api.route("/video/<code>")
def videoSource(code):
    return video_get_source(code)