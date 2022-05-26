import datetime
import json

from pytfsclient.tfs_workitem_model import TfsWorkitem

from app_modules.tfsclient import tfsclient

with open('queries.json') as queries:
    QUERIES = json.load(queries)


class User:
    def __init__(self, user: dict):
        self.name = user['displayName']
        self.url = user['url']
        self.id = user['id']
        self.domain_name = user['uniqueName']
        self.avatar = user['imageUrl']

    def __repr__(self):
        return f"Id: {self.id}, Name: {self.name}, Domain Name: {self.domain_name}"

    def __str__(self):
        return f"{self.name}"


class WorkItem:
    def __init__(self, wi: TfsWorkitem):
        self.id = wi.id
        self.title = wi.title
        self.assigned_to = User(wi['System.AssignedTo'])
        self.description = wi.description
        self.type = wi.type_name
        self.url = wi.url
        self.iteration = wi['System.IterationPath']
        self.area = wi['System.AreaPath']
        self.project = wi['System.TeamProject']
        self.parent_id = wi['System.Parent']
        self.state = wi['System.State']
        self.reason = wi['System.Reason']
        self.priority = wi['Microsoft.VSTS.Common.Priority']
        self.prio_index = wi['KL.PrioIndexDouble']
        self.analysis_expected_date = self.get_date_from_tfsstrdate(wi['KL.AnalysisExpectedDate'])
        self.analysis_ready_date = self.get_date_from_tfsstrdate(wi['KL.AnalysisReadyDate'])
        self.resolve_expected_date = self.get_date_from_tfsstrdate(wi['KL.RND.ExpectedResolveDate'])
        self.resolve_ready_date = self.get_date_from_tfsstrdate(wi['KL.RND.ExpectedDevResolveDate'])

    def __repr__(self):
        return f"Id: {self.id}, Type: {self.type}, Title: {self.title}"

    def __str__(self):
        return f"{self.type}: {self.title}"

    def get_date_from_tfsstrdate(self, tfs_date: str):
        if tfs_date:
            return datetime.date.fromisoformat(tfs_date.rsplit('T')[0])
        else:
            return None


class WorkItems:
    def __init__(self, query_name: str=None, workitems: list=None):
        if query_name:
            workitems = self.get_workitems_from_wiql(query_name)
        elif workitems:
            pass
        else:
            raise ValueError('At least one must be submitted: query_name or workitems')

        self.tasks = []
        self.bugs = []
        self.crs = []
        self.brqs = []

        for workitem in workitems:
            wi = WorkItem(workitem)
            if wi.type == 'Task':
                self.tasks.append(wi)
            elif wi.type == 'Requirement':
                self.brqs.append(wi)
            elif wi.type == 'Change Request':
                self.crs.append(wi)
            elif wi.type == 'Bug':
                self.bugs.append(wi)

    def get_workitems_from_wiql(self, query_name: str):
        wiql_result = tfsclient.wi_client.run_wiql(QUERIES[query_name])
        if wiql_result.is_empty:
            workitems = None
        else:
            workitems = wiql_result.workitems
        return workitems


# class IndexWorkItems(WorkItems):
#     def __init__(self):
#         self.tasks = self.get_workitems_from_wiql('main_window_tasks_query')
#         self.bugs = self.get_workitems_from_wiql('main_window_bugs_query')
#         self.crs = self.get_workitems_from_wiql('main_window_crs_query')
#         self.brqs = self.get_workitems_from_wiql('main_window_brqs_query')
# TODO: этот класс не нужен, перенести запросы в route