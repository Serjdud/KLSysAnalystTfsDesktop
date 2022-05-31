import json

from flask import Flask


app = Flask(__name__)

from app_modules import routes, jinja_filters

if __name__ == '__main__':
    app.run()
