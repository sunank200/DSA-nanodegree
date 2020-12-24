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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def check_area_code(area_code, telephone_number):
    if telephone_number.startswith(area_code):
        return True
    return False


def getCode(telephone_number):
    if telephone_number.startswith("140"):
        return "140"
    elif telephone_number.startswith(("7", "8", "9")):
        return telephone_number[0:4]
    else:
        temp_list = telephone_number.split(")")
        return temp_list[0] + ")"


def numberCalledByPeopleInArea(area_code):
    list_of_codes = set()
    to_bangalore = 0
    to_other = 0
    for each_call in calls:
        if check_area_code(area_code, each_call[0]):
            list_of_codes.add(getCode(each_call[1]))
            if getCode(each_call[1]).startswith("(080)"):
                to_bangalore += 1
            else:
                to_other += 1

    print("The numbers called by people in Bangalore have codes:")

    list_of_codes = list(list_of_codes)
    list_of_codes.sort()
    for code in list_of_codes:
        print(code)

    print(
        "{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
            round(float((to_bangalore / (to_other + to_bangalore)) * 100), 2)
        )
    )


numberCalledByPeopleInArea("(080)")
