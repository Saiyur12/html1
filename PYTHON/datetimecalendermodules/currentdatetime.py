

from datetime import date , time , datetime


# calling the today
#calling of data class
today = date.today()
now = datetime.now()
print("Today's date is", today)
print("\nCurrent Date and Time is ", now)


# Printing date's components 
print("\nDate components", today.year, today.month, today.day)