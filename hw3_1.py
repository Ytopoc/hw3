from datetime import datetime
def get_days_from_today(udate):
    today = datetime.today().date()
    try:
        data_gotovo = datetime.strptime(udate, '%Y-%m-%d')
    except ValueError:
        return print("Не коректна дата")
    difference = today - data_gotovo.date()
    return difference.days
date_1 = '2020-10-09'
print(get_days_from_today(date_1))

 
