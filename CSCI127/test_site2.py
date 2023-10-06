print("Please enter a date")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

print("Menu: ")
print("1)  Calculate the number of days in the given month.")
print("2)  Calculate the number of days left in the given year.")
inp = int(input(""))


def leap_year(x):
    if x%4 == 0:
        return 1
    else:
        return 0

def number_of_days(x, y):
    days_dic = {"1": 31, "2": 28,
                    "3": 31, "4": 30,
                    "5": 31, "6": 30,
                    "7": 31, "8": 31,
                    "9": 30, "10": 31,
                    "11": 30, "12": 31}
    if leap_year(y) == 0:
        return days_dic[str(x)]
    elif x == 2:
        return 29
    else:
        return days_dic[str(x)]


def days_left(d, m, y):
    days_dic = {"1": 31, "2": 28,
                    "3": 31, "4": 30,
                    "5": 31, "6": 30,
                    "7": 31, "8": 31,
                    "9": 30, "10": 31,
                    "11": 30, "12": 31}
    lst = []
    lst_sum = []
    if y%4 != 0:
        for i in range(1, m):
            lst_sum.append(days_dic[str(i)])
        ds = sum(lst_sum)
        dsf = ds + (days_dic[str(m)] - d)
        return 365 - dsf
    else:
        days_dic = {"1": 31, "2": 29,
                    "3": 31, "4": 30,
                    "5": 31, "6": 30,
                    "7": 31, "8": 31,
                    "9": 30, "10": 31,
                    "11": 30, "12": 31}
        for i in range(1, m):
            lst_sum.append(days_dic[str(i)])
        ds = sum(lst_sum)
        dsf = ds + (days_dic[str(m)] - d)
        return 366 - dsf


if inp == 1:
    print(number_of_days(month, year))
elif inp == 2:
    print(days_left(day, month, year))



