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
    all_number_with_text_records = set()
    all_numbers_receving_incoming_calls = set()

    for each_text in texts:
        all_number_with_text_records.add(each_text[0])
        all_number_with_text_records.add(each_text[1])

    for each_call in calls:
        all_numbers_receving_incoming_calls.add(each_call[1])

    telemarketer_numbers = set()
    for each_call in calls:
        if each_call[0] not in all_numbers_receving_incoming_calls:
            if each_call[0] not in all_number_with_text_records:
                telemarketer_numbers.add(each_call[0])

    telemarketer_numbers = list(telemarketer_numbers)
    telemarketer_numbers.sort()
    print("These numbers could be telemarketers: ")
    for telephone_number in telemarketer_numbers:
        print(telephone_number)


listOfTelemarketers()
