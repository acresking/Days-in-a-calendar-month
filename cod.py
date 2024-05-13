def create_calendar(year):
    calendar = {}
    months = ['ינואר', 'פברואר', 'מרץ', 'אפריל', 'מאי', 'יוני', 'יולי', 'אוגוסט', 'ספטמבר', 'אוקטובר', 'נובמבר', 'דצמבר']
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(12):
        if i == 1 and is_leap_year(year):
            days_in_month[i] = 29
        calendar[months[i]] = days_in_month[i]
    return calendar

def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

year = int(input("Enter a year: "))
calendar = create_calendar(year)
print("לוח שנה עבור השנה {}".format(year))
for month, days in calendar.items():
    print("{}: {} ימים".format(month, days))
