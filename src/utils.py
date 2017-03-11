import datetime


formatStr = '%Y%m%d'


def today():
    today_date = datetime.date.today()
    return today_date.strftime(formatStr)


def yesterday():
    today_date = datetime.date.today()
    delta_date = datetime.timedelta(days=1)
    yesterday_date = today_date - delta_date
    return yesterday_date.strftime(formatStr)