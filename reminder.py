from datetime import datetime
import time
#from dateutil import parser #to get date from user
#date = parser.parse(input("Enter date: "))

label=input('Enter the label for the remainder: ')

date_time = str(input('Enter date and time: (yyyy-mm-dd hh:mm): '))
my_date = datetime.strptime(date_time, "%Y-%m-%d %H:%M")

# datetime object containing current date and time
now_date = datetime.now()
# dd/mm/YY H:M:S
#now_date = now.strptime(now, "%d/%m/%Y %H:%M:%S")


remaining_time=(my_date - now_date).total_seconds()

time.sleep(remaining_time)
print(label)
