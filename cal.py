#Sure, here is a simple Python code that displays a calendar for a specified month and year:

#```python
import calendar

def display_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    
    # Print the month and year
    print(calendar.month_name[month], year)
    
    # Print the days of the week
    print("Mo Tu We Th Fr Sa Su")
    
    # Print each week of the month
    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end="")
            else:
                print(f"{day:2} ", end="")
        print()

# Input month and year
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Display the calendar
display_calendar(year, month)
#```

#You can run this code and enter the desired year and month to see a calendar displayed in the console.