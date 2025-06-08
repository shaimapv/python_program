import datetime
year=int(input("Enter the year for which you want to display the calendar: "))
month=int(input("Enter the month in number (1-12):"))

first_day=datetime.date(year,month,1)

if month == 12:
    next_month = datetime.date(year + 1, 1, 1)
else:
    next_month = datetime.date(year, month + 1, 1)

days_in_month = (next_month - first_day).days
print("\nMo Tu We Th Fr Sa Su")
start_weekday = first_day.weekday() 
day = 1
print("   " * start_weekday, end="")
for i in range(start_weekday, start_weekday + days_in_month):
    print(f"{day:2d} ", end="")
    if (i + 1) % 7 == 0:
        print()
    day += 1

print()

"""
Output:

PS C:\training\3rd task> python date_time.py
Enter the year for which you want to display the calendar: 2025
Enter the month in number (1-12):6

Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30
"""