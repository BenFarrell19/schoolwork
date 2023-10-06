import string


# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Presidents                 |
# Ben Farrell                           |
# Last Modified: Month 11, 2021         |
# ---------------------------------------
# an indexing searchable presidential database
# ---------------------------------------

# Your solution goes here ...

class President:
    def __init__(self, first, last, number, start_in, term, occupations):
        self.last = last
        self.name = first + ' ' + last
        self.number = number
        self.start_in = start_in
        self.term = term
        self.occupations = occupations

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_occupation(self):
        return self.occupations

    def get_time_in_office(self):
        return self.term

    def __str__(self):
        return f'President({self.last}, {self.name}, {self.number}, {self.start_in}, {self.term}, {self.occupations})'


# ---------------------------------------

def print_menu():
    print("""
1. Print all presidents
2. Print president by name
3. Print president by number
4. Count presidents with occupation
5. Print average term length
6. Quit
    """)


# ---------------------------------------
# printing every president in file
def print_all_presidents(pres_listing):
    for president in pres_listing:
        print("No. " + str(president.number), "(" + str(president.start_in) + ")", president.name)


# print president with matching last names
def print_by_name(pres_listing, name):
    if len(name) < 3:
        name = input("Enter a name longer than three characters: ")
    rtrn_lst = []
    for president in pres_listing:
        if president.last.lower() == name.lower():
            rtrn_lst.append([president.number, president.start_in, president.name])
    if len(rtrn_lst) > 0:
        for i in rtrn_lst:
            print("No.", i[0], "(" + str(i[1]) + ")", i[2])
    else:
        print("\nNo president's name contains " + repr(name))


# print presidents by their index number, or number since first president
def print_by_number(pres_listing, num):
    if 0 < num < 46:
        for president in pres_listing:
            if president.number == num:
                return print("\nNo.", president.number, "(" + str(president.start_in) + ")", president.name)
    else:
        print("\nPresident number must be between 1 and 46 ")


# print presidents with a certain occupation
def count_by_occupation(pres_listing, occupation):
    pres_returns = []
    for president in pres_listing:
        for occ in president.occupations:
            if occ.lower() == occupation.lower():
                pres_returns.append(president.name)
    return print("\n" + str(len(set(pres_returns))), occupation + ' presidents:', ', '.join(set(pres_returns)))


# calculating the average presidential term length
def average_term_length(pres_listing):
    terms = []
    for president in pres_listing:
        terms.append(president.term)
    return print("\nAverage term length, about " + str(round(sum(terms) / len(terms), 0)) + " years")


# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pres_listing(filename):
    pres_listing = []
    file = open(filename, "r")

    for president in file:
        presilist = president.strip().split(",")
        number = int(presilist[0])  # number
        last = presilist[1]  # last name
        first = presilist[2]  # first name
        start_in = int(presilist[3])  # first year in office
        term = float(presilist[4])  # years in office
        occupations = []
        for position in range(5, len(presilist)):
            occupations += [presilist[position]]  # occupation
        pres_listing += [President(first, last, number, start_in, term, occupations)]

    file.close()
    return pres_listing


# ---------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    answer = input(message)
    while answer == "":
        answer = input(message)
    for char in answer:
        if char not in string.digits:
            print('ERROR: ', answer, "is not a number")
            return 0
    answer = int(answer)
    if (low > answer) or (answer > high):
        print('ERROR: ', answer, "is not a choice")
        return 0

    return answer


# ---------------------------------------

def main():
    pres_listing = create_pres_listing("pres_listing.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:
            print_all_presidents(pres_listing)
        elif choice == 2:
            name = input("Enter a president name: ").lower()
            print_by_name(pres_listing, name)
        elif choice == 3:
            number = get_choice(1, 46, "Enter a president number: ")
            print_by_number(pres_listing, number)
        elif choice == 4:
            occupation = input("Enter a president occupation: ").lower()
            count_by_occupation(pres_listing, occupation)
        elif choice == 5:
            average_term_length(pres_listing)
        elif choice == 6:
            print("Thank you.  Goodbye!")


# ---------------------------------------

main()
