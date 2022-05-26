from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    wi = IndexWorkItems() # TODO: переписать на создание объекта WorkItems с использованием запросов
    return render_template('index.html', title='Main', wi=wi)


if __name__ == '__main__':
    app.run()
