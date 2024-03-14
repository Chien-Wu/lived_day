import datetime
bday = input("what is your bday (dd/mm/yyyy)")
list = bday.split("/")
born_year = int(list[2])
born_month = int(list[1])
born_day = int(list[0])

current_date = datetime.date.today()
current_year = int(current_date.year)
current_month = int(current_date.month)
current_day = int(current_date.day)

if born_month > current_month:
    lived_year = current_year - born_year - 1
    lived_month =  12 + current_month - born_month
elif born_month == current_month:
    if born_day > current_day:
        lived_year = current_year - born_year
    elif born_day < current_day:
        lived_year = current_year - born_year 
    else:
        lived_year = current_year - born_year
        print("happy",lived_year, "th birthday")
elif born_month < current_month:
    lived_year = current_year - born_year
    lived_month = current_month - born_month

lived_day = current_day
print("you have lived", lived_year, "years,", lived_month, "month,", lived_day, "days")