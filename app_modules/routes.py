from flask import render_template

from app import app
from app_modules.wi_constructor import WorkItems
from app_modules.wiql_query_constructor import QUERIES


@app.route('/')
@app.route('/index')
def index():
    own_new_tasks = WorkItems(QUERIES['own_new_tasks']).tasks
    own_overdue_tasks = WorkItems(QUERIES['own_overdue_tasks']).tasks
    own_bugs_1prio = WorkItems(QUERIES['own_bugs_1prio']).bugs
    own_bugs_2prio = WorkItems(QUERIES['own_bugs_2prio']).bugs
    own_new_crs = WorkItems(QUERIES['own_new_crs']).crs
    own_new_brqs = WorkItems(QUERIES['own_new_brqs']).brqs
    own_overdue_crs = WorkItems(QUERIES['own_overdue_crs']).crs
    return render_template('index.html', title='Main',
                           own_new_tasks=own_new_tasks,
                           own_overdue_tasks=own_overdue_tasks,
                           own_bugs_1prio=own_bugs_1prio,
                           own_bugs_2prio=own_bugs_2prio,
                           own_new_crs=own_new_crs,
                           own_overdue_crs=own_overdue_crs,
                           own_new_brqs=own_new_brqs)


@app.route('/bugs')
def own_bugs():
    own_bugs_1prio = WorkItems(QUERIES['own_bugs_1prio']).bugs
    own_bugs_2prio = WorkItems(QUERIES['own_bugs_2prio']).bugs
    own_bugs_3prio = WorkItems(QUERIES['own_bugs_3prio']).bugs
    return render_template('bugs/own_bugs.html', title='Bugs',
                           own_bugs_1prio=own_bugs_1prio,
                           own_bugs_2prio=own_bugs_2prio,
                           own_bugs_3prio=own_bugs_3prio)


@app.route('/tasks')
def own_tasks():
    own_new_tasks = WorkItems(QUERIES['own_new_tasks']).tasks
    own_overdue_tasks = WorkItems(QUERIES['own_overdue_tasks']).tasks
    own_active_tasks = WorkItems(QUERIES['own_active_tasks']).tasks
    return render_template('tasks/own_tasks.html', title='Tasks',
                           own_new_tasks=own_new_tasks,
                           own_overdue_tasks=own_overdue_tasks,
                           own_active_tasks=own_active_tasks)


@app.route('/crs')
def own_crs():
    own_new_crs = WorkItems(QUERIES['own_new_crs']).crs
    own_overdue_crs = WorkItems(QUERIES['own_overdue_crs']).crs
    own_active_crs = WorkItems(QUERIES['own_active_crs']).crs
    return render_template('crs/own_crs.html', title='CRs',
                           own_new_crs=own_new_crs,
                           own_overdue_crs=own_overdue_crs,
                           own_active_crs=own_active_crs)


@app.route('/brqs')
def own_brqs():
    own_new_brqs = WorkItems(QUERIES['own_new_brqs']).brqs
    own_active_brqs = WorkItems(QUERIES['own_active_brqs']).brqs
    return render_template('brqs/own_brqs.html', title='BRQs',
                           own_new_brqs=own_new_brqs,
                           own_active_brqs=own_active_brqs)
