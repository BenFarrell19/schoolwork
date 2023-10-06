# --------------------------------------
# CSCI 127, Lab 6                      |
# Month 10, 2021                     |
# Ben Farrell                            |
# --------------------------------------
# Counting word frequencies           |
# --------------------------------------

import re


def make_word_list(user_input):
    user_input = user_input.lower()
    user_input = re.sub(r'[^\w\s]', '', user_input)
    user_input = user_input.split()
    print(user_input)
    return user_input


def count_freq(words):
    lst = []
    for i in words:
        if i in lst:
            continue
        lst.append(i)
        c = 0
        for x in words:
            if i == x:
                c += 1
        if c == 1:
            print(i.upper(), "appears once.")
        elif c == 2:
            print(i.upper(), "appears twice.")
        else:
            print(i.upper(), "appears", c, "times.")


def main():
    user_input = input("Enter words: ")
    words = make_word_list(user_input)
    print("Word Counts:")
    count_freq(words)


main()
