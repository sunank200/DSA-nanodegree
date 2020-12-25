"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

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


def listOfTelemarketers():
    all_caller = set()
    other_numbers = set()

    for each_text in texts:
        other_numbers.add(each_text[0])
        other_numbers.add(each_text[1])

    for each_call in calls:
        other_numbers.add(each_call[1])
        all_caller.add(each_call[0])

    telemarketer_numbers = all_caller - other_numbers

    print("These numbers could be telemarketers: ")
    for telephone_number in sorted(telemarketer_numbers):
        print(telephone_number)


listOfTelemarketers()
