import datetime

from app import app


@app.template_filter('compare_date_with_today')
def compare_date_with_today(date: datetime.date) -> bool:
    if date and date < datetime.date.today():
        return True
    else:
        return False
