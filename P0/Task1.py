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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""


def differentPhoneNumbers():
    set_of_phone_numbers = set()
    for each_text in texts:
        set_of_phone_numbers.add(each_text[0])
        set_of_phone_numbers.add(each_text[1])

    for each_call in calls:
        set_of_phone_numbers.add(each_call[0])
        set_of_phone_numbers.add(each_call[1])

    print(
        "There are {} different telephone numbers in the records.".format(
            len(set_of_phone_numbers)
        )
    )


differentPhoneNumbers()
