import datetime

from pytfsclient.tfs_workitem_model import TfsWorkitem

from app_modules.tfsclient import tfsclient


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
        self.estimation_expected_date = self.get_date_from_tfsstrdate(wi['KL.EstimationExpectedDate'])
        self.estimation_ready_date = self.get_date_from_tfsstrdate(wi['KL.EstimationReadyDate'])

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
    def __init__(self, query: str=None, _workitems: list=None):
        if query and not _workitems:
            _workitems = self.get_workitems_from_wiql(query)
        elif _workitems and not query:
            pass
        else:
            raise ValueError('One argument must be submitted: query_name or workitems')

        self.tasks = []
        self.bugs = []
        self.crs = []
        self.brqs = []

        if _workitems:
            for _workitem in _workitems:
                _wi = WorkItem(_workitem)
                if _wi.type == 'Task':
                    self.tasks.append(_wi)
                elif _wi.type == 'Requirement':
                    self.brqs.append(_wi)
                elif _wi.type == 'Change Request':
                    self.crs.append(_wi)
                elif _wi.type == 'Bug':
                    self.bugs.append(_wi)

    def get_workitems_from_wiql(self, query: str):
        _wiql_result = tfsclient.wi_client.run_wiql(query)
        if _wiql_result.is_empty:
            _workitems = None
        else:
            _workitems = _wiql_result.workitems
        return _workitems
