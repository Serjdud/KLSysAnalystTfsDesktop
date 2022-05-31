import datetime

from app import app


@app.template_filter('compare_date_with_today')
def compare_date_with_today(date: datetime.date) -> bool:
    if date and date < datetime.date.today():
        return True
    else:
        return False


@app.template_filter('is_critical_bug')
def if_critical_bug(bug_priority):
    if bug_priority and bug_priority == 1:
        return True
    else:
        return False
