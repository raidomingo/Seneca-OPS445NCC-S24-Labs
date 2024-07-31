#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Summer 2024
Program: assignment1.py 
The python code in this file is original work written by
Raymond Domingo. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Raymond Domingo
Description: A script that will return an end date(inluding day of the week), given a start date and number of days
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "return true if the year is a leap year"
    ...
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    ...
    leap_flag = leap_year(year)

    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_flag:      # This is the month of february
        return 29
    else:
        return mon_dict[month]

def after(date: str) -> str: 
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day

    max_days = mon_max(mon, year)
    
    if day > max_days:
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1 
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    ...
    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1  # previous day

    max_days = mon_max(mon, year)
    
    if day == 0:    # Day 0 is the last day of the previous month
        mon -= 1    # adjusting to last month
        if mon == 0:
            year -= 1 #adjusting to last year
            mon = 12
        day = mon_max(mon, year)  # if the day is 1, next ady will reset to the last day of the last month
    return f"{day:02}/{mon:02}/{year}"

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date: Returns true if it's VALID and false if it's INVALID"
    ...
    try:
        day, mon, year = (int(x) for x in date.split('/'))
        if mon < 1 or mon > 12: # Range of valid months
            return False
        if day < 1 or day > mon_max(mon, year): #range of valid days per month
            return False
        return True
    except ValueError:
        return False
    
def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"
    ...
    cur_date = start_date
    if num >= 0:
        for _ in range(num):
            cur_date = after(cur_date)
    else:
        for _ in range(-num):
            cur_date = before(cur_date)
    return cur_date

if __name__ == "__main__":
    # check length of arguments
    # check first arg is a valid date
    # check that second arg is a valid number (+/-)
    # call day_iter function to get end date, save to x
    # print(f'The end date is {day_of_week(x)}, {x}.')
    pass