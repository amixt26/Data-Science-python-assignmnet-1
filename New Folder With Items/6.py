#to find the dya btw 2 dates
from datetime import date
def number_of_days(date1, date2):
     return(date1-date2).days

date1 = date (2023,9,10)
date2 = date (2023,10,10)

print(number_of_days(date1,date2))