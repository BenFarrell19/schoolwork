# --------------------------------------
# CSCI 127, Program 3                  |
# Month 10, 2021                       |
# Ben Farrell                          |
# --------------------------------------

import pandas as pd


def ave_infection_rate(file_name):
    # create pandas dataframe
    df = pd.read_csv(file_name)
    t = 0
    # looping through case rate and creating sum
    for i in df["Data.Rate"]:
        t += i
    # calculating average
    avg = t / len(df["Data.Rate"])
    return avg


def countries_in_study(file_name, save_as):
    # create pandas dataframe

    df = pd.read_csv(file_name)
    pop_dic = {}
    # removing duplicate for list of each country
    countries = set(df["Location.Country"])

    for i in countries:
        index = df.index[df["Location.Country"] == i]
        pop_dic[i] = int(df.iloc[index[1], 7])
        # sorting from greatest to least
    pop_dic = sorted(pop_dic.items(), key=lambda x: x[1], reverse=True)
    with open(save_as, 'w') as f:
        # removing last row with negative values
        pop_dic = pd.DataFrame(pop_dic).shift()[1:-1]
        # formatting for output file
        f.write(pd.DataFrame.to_csv(pop_dic, header=None, index=True, sep=' ', line_terminator='\n'))
    f.close()


def deaths_in_country(file_name, country):
    # create pandas dataframe
    dic = {}
    df = pd.read_csv(file_name)
    countries = set(df["Location.Country"])
    for e in countries:
        deaths = 0
        # looping through each countries row numbers and summing number of deaths
        for i in df.index[df['Location.Country'] == e]:
            deaths += df['Data.Deaths'][i]
        dic[e] = deaths
    # I know this isn't the most straight forward way to do this but figured it may be helpful do have a dictionary of the deaths to access
    return dic[country]


# --------------------------------------

def main(file_name):
    print("Global data collected between Jan 1 - Nov 5, 2020".center(50))
    infections = ave_infection_rate(file_name)
    print('*' * 50)
    print("Fortnightly cases reported per 100,000 people,\n(global average): ", end="")
    print(ave_infection_rate(file_name))

    print('*' * 50)
    user_input = input("Save list countries? ('y' for yes) : ")
    if user_input.lower() == 'y':
        save_as = input("Save File As: ")
        save_as += ".txt"
        countries_in_study(file_name, save_as)
        print("File saved as", save_as)

    print('*' * 50)
    country = input("Enter a country in the dataset: ")
    num = deaths_in_country(file_name, country)
    print("The data reports {:d} covid deaths in {}.".format(num, country))

    print('*' * 50)



# --------------------------------------

main("covid.csv")
