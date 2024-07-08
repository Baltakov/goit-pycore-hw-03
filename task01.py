from datetime import datetime

def get_days_from_today(date):
    given_date = datetime.strptime(date, '%Y-%m-%d')
    
    today = datetime.today().date()
    given_date = given_date.date()
    
    delta = today - given_date
    
    return delta.days

print(get_days_from_today('2021-10-09')) 
print(get_days_from_today('2025-10-09')) 
