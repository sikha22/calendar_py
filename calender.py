""" to display the calendar of a given month and year by the user """
import calendar
y = int(input("Enter year: "))  
m  = int(input("Enter month: "))
print(calendar.month(y,m))  