from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() in [5, 6]:
                while birthday_this_year.weekday() != 0:
                    birthday_this_year += timedelta(days=1)
            
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "Alice", "birthday": "1990.06.24"},
    {"name": "Bob", "birthday": "1985.06.27"},
    {"name": "Charlie", "birthday": "1979.06.30"},
    {"name": "David", "birthday": "1992.07.01"},
    {"name": "Eva", "birthday": "1995.07.04"}
]

print(get_upcoming_birthdays(users))
