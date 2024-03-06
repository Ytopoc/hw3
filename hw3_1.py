from datetime import datetime, timedelta , date
# Обробка вийнятків, і створення дати клієнта
def test_udate():
    def comeback_year(): 
        global uyear
        try:
            uyear= int(input("Введіть рік у форматі РРРР:"))
        except ValueError: print("Ви не коректно ввели рік"), comeback_year()
    comeback_year()
    test_uyear = len(str(uyear))
    if test_uyear > 4 or uyear== 0 :
        comeback_year()
        print("Ви не коректно ввели рік")
    def comeback_month():
        global umonth 
        try:
            umonth= int(input("Введіть місяц у форматі ММ:"))
        except ValueError: print("Ви не коректно ввели місяць"), comeback_month()
    comeback_month()
    if umonth > 12 or umonth== 0 :
        print("Такого місяця не існує")
        comeback_month()
    def comeback_day():
        global uday
        try:
            uday= int(input("Введіть день у форматі ДД:"))
        except ValueError: print("Ви не коректно ввели день"), comeback_day()
    comeback_day()
    if uday > 31 or uday== 0  :
        comeback_day()
        print("Такого дня не існує")
    global your_date
    try:
        your_date= date(year=uyear, month=umonth, day=uday)
    except ValueError: print("Такої дати не існує"), test_udate()


test_udate() #Запуск функції
def get_days_from_today(u_date):
    now= date.today() #Створення сьогоднішньої дати

    example = now - u_date #Різниця дат
    example_int = example.days #Перетворення відповіді у тип int
    print(f"Різня між {now} і {u_date} дорівнює {example_int} днів")
    return example_int
get_days_from_today(your_date)
#Я зрозумів що завдання зробив не так як треба, але я це помітив, коли вже зробив. Пробачте 
 
