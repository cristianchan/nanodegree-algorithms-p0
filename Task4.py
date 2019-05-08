"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    

telemarketers = set()

texts_from_numbers = [row[0] for row in texts]
texts_to_numbers = [row[0] for row in texts]
calls_to_numbers = [row[1] for row in calls]

for call in calls:
    if call[0] not in texts_from_numbers and call[0] not in texts_to_numbers and call[0] not in calls_to_numbers:
        telemarketers.add(call[0])

print("These numbers could be telemarketers: ")
for number in sorted(telemarketers):
    print(number)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

