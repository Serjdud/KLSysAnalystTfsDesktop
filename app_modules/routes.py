import json

from flask import render_template

from app import app
from app_modules.wiconstructor import WorkItems

with open('queries.json') as queries:   # TODO: сделать более удобочитаемый JSON и сделать конструктор wiql-запроса из JSONа
    QUERIES = json.load(queries)


@app.route('/')
@app.route('/index')
def index():
    my_new_tasks = WorkItems(QUERIES['my_new_tasks']).tasks
    my_overdue_tasks = WorkItems(QUERIES['my_overdue_tasks']).tasks
    my_active_bugs = WorkItems(QUERIES['my_active_bugs']).bugs  # TODO: разделить баги на 1, 2 и 3 приоритет
    my_new_crs = WorkItems(QUERIES['my_new_crs']).crs
    my_new_brqs = WorkItems(QUERIES['my_new_brqs']).brqs
    my_overdue_crs = WorkItems(QUERIES['my_overdue_crs']).crs
    return render_template('index.html', title='Main',
                           my_new_tasks=my_new_tasks,
                           my_overdue_tasks=my_overdue_tasks,
                           my_new_bugs=my_active_bugs,
                           my_new_crs=my_new_crs,
                           my_overdue_crs=my_overdue_crs,
                           my_new_brqs=my_new_brqs)
