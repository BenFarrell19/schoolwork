# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Lab 3: Season Checker
# Ben Farrell
# Last Modified: Month 09, 2021
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------
import pandas as pd
import datetime as dt

spring = {"start": "03/20/2015", "end": "06/20/2015"}
summer = {"start": "06/21/2015", "end": "09/21/2015"}
fall = {"start": "09/22/2015", "end": "12/20/2015"}
winter = {"start": "12/21/2015", "end": "03/19/2016"}


# TODO: write a function called season_checker that returns
#  a string: Spring, Summer, Winter, Fall, or Invalid
def season_checker(month, day, year=2015):
    if str(dt.date(year, month, day)) in pd.date_range(spring['start'], spring['end']):
        return "That's a spring day"
    if str(dt.date(year, month, day)) in pd.date_range(summer['start'], summer['end']):
        return "That's a summer day"
    if str(dt.date(year, month, day)) in pd.date_range(fall['start'], fall['end']):
        return "That's a fall day"
    if str(dt.date(year, month, day)) in pd.date_range(winter['start'], winter['end']):
        return "That's a winter day"


def main():
    try:
        user_month = dt.datetime.strptime(input("Enter month: "), "%B").month
        user_day = int(input("Enter day: "))
        season = season_checker(user_month, user_day)
        print(season)
    except ValueError as e:
        print("That's an unrecognized date")
        quit()
    # TODO: output the season for the user in a print statement,
    # or tell them if they input an invalid date


main()
