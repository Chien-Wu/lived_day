import datetime
current_date = datetime.date.today()

bday = input("enter your birthday(dd/mm/yyyy):")
data = bday.split("/")
day = datetime.date(int(data[2]), int(data[1]), int(data[0]))
lived_day = current_date - day

print("you have lived",lived_day.days, "days")
print("you have lived",lived_day.total_seconds(), "seconds")