from flask import Flask
from router.home import home
from router.api import api

app = Flask(__name__,
            template_folder="views",
            static_folder="public")

app.register_blueprint(home)
app.register_blueprint(api,url_prefix="/api")

app.run(debug=True)