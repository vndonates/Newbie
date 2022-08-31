#Countdown to election day
from datetime import *

#Get Today's Date
today = date.today()
print("Today: " + today.strftime('%b %d, %Y'))

#Find out how many days until Election Day:
thisYear = today.year
election_day = date(thisYear,11,8) # Nov 8

if today < election_day:
    print("Next Election Day: " + election_day.strftime('%b %d, %Y'))
    #Calculate number of days until Election Day
    delta = (election_day - today).days
    print(str(delta) + " days left until Election Day!")
elif today == election_day:
    print("Today is Election Day!")
else:
    #We've passed this year's Election Day, we will need to wait for next year!
    next_election_day = date(thisYear+1,11,7) # Nov 7, 2023
    print("Next Election Day: " + next_election_day.strftime('%b %d, %Y'))
    delta = (next_election_day - today).days
    print(str(delta) + " days left until next Election Day!")
