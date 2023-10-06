# --------------------------------------
# CSCI 127, Lab 5                      |
# Month 09, 2021                     |
# Ben Farrell                            |
# --------------------------------------
# Calculate how many vowels are in a   |
# sentence using three techniques.     |
# --------------------------------------

vowels = ['a', 'e', 'i', 'o', 'u']


def count_built_in(sentence):
    c = 0
    sentence = sentence.lower()
    for i in vowels:
        c += sentence.count(i)
    return c


def count_iterative(sentence):
    c = 0
    for i in sentence.lower():
        if i in vowels:
            c += 1
    return c


def is_vowel(letter):
    if letter.lower() in vowels:
        return 1
    else:
        return 0


def count_recursive(sentence):
    if len(sentence) == 1:
        return is_vowel(sentence[0])
    return count_recursive(sentence.replace(sentence[0], "", 1)) + is_vowel(sentence[0])


# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        sentence = sentence.lower()
        print()
        print("Calculating the number of vowels  using ...")
        print("-------------------------------------------")
        print("Built-in function =", count_built_in(sentence))
        print("Iteration =", count_iterative(sentence))
        print("Recursion =", count_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()


# --------------------------------------

main()
