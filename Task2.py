"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import operator
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

call_duration = defaultdict(int)

for call in calls:
    call_duration[call[0]] += int(call[3])
    call_duration[call[1]] += int(call[3])


max_phone_call = max(call_duration.items(), key=operator.itemgetter(1))

print('%s spent the longest time, %s seconds, on the phone during September 2016.'%(max_phone_call[0],max_phone_call[1]))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

