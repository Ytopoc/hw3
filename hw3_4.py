from datetime import timedelta , datetime
def get_upcoming_birthdays(slovar):
    prepared_users = []
    try:
        for kolega in slovar:
            birthday_data = datetime.strptime(kolega["birthday"], "%Y.%m.%d").date()
            prepared_users.append({"name": kolega['name'], "birthday":birthday_data})
    except ValueError:
        print("Не коректна дата народження")
    today=datetime.today().date()
    days = 7
    upcoming_birth = []
    def find_next_weekday(d , weekday: int):
        days_ahead =weekday -d.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return d + timedelta(days=days_ahead) 
    for kolega in prepared_users: 
        this_year_birth = kolega['birthday'].replace(year=today.year)
        if this_year_birth < today:
            this_year_birth = this_year_birth.replace(year=today.year +1)
        if 0 <= (this_year_birth- today).days <= days:
            if this_year_birth.weekday() >= 5:
                this_year_birth = find_next_weekday(this_year_birth, 0)
            congratulation = this_year_birth.strftime("%Y.%m.%d")
            upcoming_birth.append({"name": kolega["name"], "congratulation_date": congratulation})
    return upcoming_birth
users = [
    {"name": "John Doe", "birthday": "1985.03.8"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

print(get_upcoming_birthdays(users))

