from datetime import datetime
import pytz


Portland = pytz.timezone('America/Los_Angeles')
Portland_now = datetime.now(Portland).time()

NY = pytz.timezone('America/New_York')
NY_now = datetime.now(NY).time()

London = pytz.timezone('Europe/London')
London_now = datetime.now(London).time()

print(Portland_now)
print(NY_now)
print(London_now)

open_time = datetime.strptime("09:00:00", "%H:%M:%S").time()
close_time = datetime.strptime("17:00:00", "%H:%M:%S").time()

if open_time <= Portland_now <= close_time:
    print("Portland branch is open")
else:
    print("Portland branch is closed")

if open_time <= NY_now <= close_time:
    print('NY Branch is open')
else:
    print('NY branch is closed')

if open_time <= London_now <= close_time:
    print('London Branch is open')
else:
    print('London branch is closed')


