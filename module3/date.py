from datetime import datetime, timedelta

def get_days_from_today(date):
    # for valid input date, transform str into date object
    try:
        start_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return print("Please, use valid format '%Y-%m-%d'")
        
    current_date = datetime.today()
    diff = current_date.toordinal() - start_date.toordinal()
    print(start_date , current_date, diff, type(diff))

get_days_from_today('2024-01-20')    