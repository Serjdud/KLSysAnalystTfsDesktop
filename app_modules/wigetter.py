import json
from app_modules.tfsclient import tfsclient

with open('queries.json') as queries:
    QUERIES = json.load(queries)


class WorkItems:
    def get_workitems(self, query_name):
        wiql_result = tfsclient.wi_client.run_wiql(QUERIES[query_name])
        if wiql_result.is_empty:
            workitems = None
        else:
            workitems = wiql_result.workitems
        return workitems


class IndexWorkItems(WorkItems):
    def __init__(self):
        self.tasks = self.get_workitems('main_window_tasks_query')
        self.bugs = self.get_workitems('main_window_bugs_query')
        self.crs = self.get_workitems('main_window_crs_query')
        self.brqs = self.get_workitems('main_window_brqs_query')

