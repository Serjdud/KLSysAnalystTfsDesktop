from flask import Flask, render_template
from app_modules.wigetter import IndexWorkItems

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    wi = IndexWorkItems()
    return render_template('index.html', title='Main', wi=wi)


if __name__ == '__main__':
    app.run()
