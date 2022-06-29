import datetime
import calendar

print()
today_year = int(input(" enter today_year:"))
today_month = int(input("enter today_month:"))
today_date = int(input("enter today_date:"))
print()

birth_year = int(input(" enter birth_year:"))
birth_month = int(input(" enter birth_year:"))
birth_date = int(input(" enter birth_year:"))
print()

a=datetime.datetime(today_year,today_month,today_date)
o=datetime.datetime(birth_year,birth_month,birth_date)

f=a.year
d=o.year

m = a.month
n = o.month

years = f-d
print("number of years , you lived in the world :",years)
print()

month = years * 12
print(" number of month , you lived in the world :",month)
print()
week = month * 4
print("number of weeks , you lived in the world:",week) 
print()
v=a-o
v = str(v)
y = v.split()

days= y[0]
print("number of days , you lived in the world:",days)
print()
hours=int(days)*24
print("number of hours , you lived in the world:",hours)
print()
minutes = hours * 60
print("number of minutes , you lived in the world:",minutes)
print()
seconds = minutes * 60
print("number of seconds , you lived in the world:",seconds)
print()


print("monthly calender of today's date !!!!!")
print()
print(calendar.month(f,m))
print()
print("monthly calender of your birth date !!!!!")
print()
print(calendar.month(d,n))
