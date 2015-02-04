from flask import Flask
import config

"""import all controller from application.controllers"""
from controllers.page import page
"""import more controller"""

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

"""register each controller as blueprint"""
app.register_blueprint(page)
"""register more controller"""

if __name__ == '__main__':
    app.debug = True
    app.run(port=config.PORT)