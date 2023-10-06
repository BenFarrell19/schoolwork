# --------------------------------------
# CSCI 127, Lab 7                      |
# Month 10, 2021                     |
# Ben Farrell                            |
# --------------------------------------
# Files - S&P 500           |
# --------------------------------------
import pandas as pd


file = r'C:\Users\Ben Farrell\Downloads\covid.csv'


def print_sectors(file_name):
    df = pd.read_csv(file_name)
    n = 0
    avg = 0
    f = 0
    l = 14
    for i in df["Data.Cases"]:
        subset = df.loc[f:l]
        n +=1
        f +=14
        l +=14
        avg += sum(subset)/14
    avg = avg/n
    return avg







def main(file_name):

    print("GICS Sectors in the S&P 500".center(50, '-'))
    print_sectors(file_name)

    print(50 * '-')
    sector = input("Enter sector: ")

    sector_list = get_securities(file_name, sector)
    heading = str(len(sector_list)) + "S&P 500 Securities in " + sector
    print(heading.center(50, '-'))
    for i in range(len(sector_list)):
        security = str(sector_list[i][0]).ljust(35, '.')
        sub_industry = sector_list[i][1]
        print(str(i+1).ljust(2), security, sub_industry)



main(sp500.csv)
'''