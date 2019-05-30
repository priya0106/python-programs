import calendar
year=int(input())
a=calendar.isleap(year)
if a==True:
    print("leap year")
else:
    print("not a leap year")
