from flask import render_template

from app import app
from app_modules.wi_constructor import WorkItems
from app_modules.wiql_query_constructor import QUERIES


@app.route('/')
@app.route('/index')
def index():
    my_new_tasks = WorkItems(QUERIES['my_new_tasks']).tasks
    my_overdue_tasks = WorkItems(QUERIES['my_overdue_tasks']).tasks
    my_bugs_1prio = WorkItems(QUERIES['my_bugs_1prio']).bugs
    my_bugs_2prio = WorkItems(QUERIES['my_bugs_2prio']).bugs
    my_new_crs = WorkItems(QUERIES['my_new_crs']).crs
    my_new_brqs = WorkItems(QUERIES['my_new_brqs']).brqs
    my_overdue_crs = WorkItems(QUERIES['my_overdue_crs']).crs
    return render_template('index.html', title='Main',
                           my_new_tasks=my_new_tasks,
                           my_overdue_tasks=my_overdue_tasks,
                           my_bugs_1prio=my_bugs_1prio,
                           my_bugs_2prio=my_bugs_2prio,
                           my_new_crs=my_new_crs,
                           my_overdue_crs=my_overdue_crs,
                           my_new_brqs=my_new_brqs)
