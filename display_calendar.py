import calendar

month = int(input("Enter a month as a number (1-12) : "))
if month <1 or month >12 :
    print("invalid month")
else:
    year = int(input("Enter the year for which you want to display the calendar: "))
    print("\n",calendar.month(year ,month))

"""
Output:
PS C:\training\3rd task> python display_calendar.py
Enter a month as a number (1-12) : 6
Enter the year for which you want to display the calendar: 2025

      June 2025
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30

"""