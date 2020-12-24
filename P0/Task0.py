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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def checkListNotEmpty(array):
    if len(array) < 1:
        return False
    return True


def printFirstTextRecord():
    assert checkListNotEmpty(texts)
    first_record = texts[0]
    print(
        "First record of texts, {} texts {} at time {}".format(
            first_record[0], first_record[1], first_record[2]
        )
    )


def printLastCallRecord():
    assert checkListNotEmpty(calls)
    last_record = calls[-1]
    print(
        "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
            last_record[0], last_record[1], last_record[2], last_record[3]
        )
    )


printFirstTextRecord()
printLastCallRecord()
