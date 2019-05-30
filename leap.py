import calendar
year=int(input())
a=calendar.isleap(year)
if a==True:
    print("yes")
else:
    print("no")
