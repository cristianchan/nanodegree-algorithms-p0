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

phone_numbers = dict()

for text in calls:
    if text[0] in phone_numbers:
        phone_numbers[text[0]] += 1
    else:
        phone_numbers[text[0]] = 1
    
    if text[1] in phone_numbers:
        phone_numbers[text[1]] += 1
    else:
        phone_numbers[text[1]] = 1

for call in calls:
    if call[0] in phone_numbers:
        phone_numbers[call[0]] += 1
    else:
        phone_numbers[call[0]] = 1
    
    if call[1] in phone_numbers:
        phone_numbers[call[1]] += 1
    else:
        phone_numbers[call[1]] = 1


print("There are %s different telephone numbers in the records."%(len(phone_numbers)))
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
