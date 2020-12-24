"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during September 2016.".
"""


def longestCall():
    call_dicts = {}
    for each_call in calls:
        if each_call[0] not in call_dicts:
            call_dicts[each_call[0]] = int(each_call[3])
        else:
            call_dicts[each_call[0]] += int(each_call[3])

        if each_call[1] not in call_dicts:
            call_dicts[each_call[1]] = int(each_call[3])
        else:
            call_dicts[each_call[1]] += int(each_call[3])

    longest_call = 0
    longest_calling_number = None
    for telephone_number in call_dicts.keys():
        if call_dicts[telephone_number] > longest_call:
            longest_call = call_dicts[telephone_number]
            longest_calling_number = telephone_number

    print(
        "{} spent the longest time, {} seconds, on the phone during September 2016.".format(
            longest_calling_number, longest_call
        )
    )


longestCall()
