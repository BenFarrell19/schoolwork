# -----------------------------------------+
# Ben Farrell                              |
# CSCI 127, Program 2                      |
# Last Updated: Month 10, 2021             |
# Name: Ben Farrell                        |
# -----------------------------------------|
# Poker Hand Evaluation                    |
# -----------------------------------------+

# Helper Function
# Given a poker hand as a list, return a list of the ranks
def get_all_ranks(hand):
    result = []
    for card in hand:
        result.append(card[0])
    return result


# TODO:
# decide on parameters for the hand evaluation functions, and
# define functions to return True if the criteria is met; false otherwise.

def royal_flush(hand):
    hand.sort()
    # check if hand contains 10-14 and all same suit
    # checks for royal flush
    t = 0
    if hand[0][0] >= 10:
        for i in range(0, 4):
            if hand[i][1] != hand[i + 1][1]:
                t = 0
                break
            else:
                t = 1

    # check for straight
    b = 0
    if t == 1:
        for i in range(0, 4):
            if hand[i][0] + 1 == hand[i + 1][0]:
                b = 1
            else:
                b = 0
                break
    if b and t == 1:
        return True
    else:
        return False


def straight_flush(hand):
    hand.sort()
    t = 0
    if hand[0][0] < 10:
        for i in range(0, 4):
            if hand[i][1] != hand[i + 1][1]:
                t = 0
                break
            else:
                t = 1

    # check for straight
    b = 0
    if t == 1:
        for i in range(0, 4):
            if hand[i][0] + 1 == hand[i + 1][0]:
                b = 1
            else:
                b = 0
                break
    if b and t == 1:
        return True
    else:
        return False


def straight(hand):
    hand.sort()
    t = 0
    for i in range(0, 4):
        if hand[i][1] != hand[i + 1][1]:
            t = 0
            break
        else:
            t = 1

    # check for straight
    b = 0
    if t != 1:
        for i in range(0, 4):
            if hand[i][0] + 1 == hand[i + 1][0]:
                b = 1
            else:
                b = 0
                break
    if b == 1:
        return True
    else:
        return False


def flush(hand):
    hand.sort()
    t = 0
    for i in range(0, 4):
        if hand[i][1] != hand[i + 1][1]:
            t = 0
            break
        else:
            t = 1

    # check for straight
    b = 0
    if t == 1:
        for i in range(0, 4):
            if hand[i][0] + 1 == hand[i + 1][0]:
                b = 1
            else:
                b = 0
                break
    if b == 0 and t == 1:
        return True
    else:
        return False


suits = ['clb', 'spd', 'dmd', 'hrt']
num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def four_of_a_kind(hand):
    if straight(hand) is False:
        for n in num:
            c = 0
            for i, j in hand:
                if i == n:
                    c += 1
            if c == 4:
                t = 1
                break
            else:
                t = 0
                continue
        if t == 1:
            return True
        else:
            return False


def full_house(hand):
    g = 0
    t = 0
    num_lst = []
    for i, j in hand:
        num_lst.append(i)

    for i in range(0, 5):
        if num_lst.count(hand[i][0]) == 3:
            g = 1
        if num_lst.count(hand[i][0]) == 2:
            t = 1

    if g and t == 1:
        return True
    else:
        return False


def three_of_a_kind(hand):
    g = 0
    num_lst = []
    for i, j in hand:
        num_lst.append(i)

    for i in range(0, 5):
        if num_lst.count(hand[i][0]) == 3:
            g = 1
    if g == 1:
        return True
    else:
        return False


def two_pair(hand):
    g = 0
    t = 0
    num_lst = []
    for i, j in hand:
        num_lst.append(i)

    for i in range(0, 5):
        if num_lst.count(hand[i][0]) == 2:
            g = 1
            num_lst.remove(hand[i][0])
            break
    for i in range(0, 5):
        if num_lst.count(hand[i][0]) == 2:
            t = 1

    if g and t == 1:
        return True
    else:
        return False



def pair(hand):
    g = 0
    num_lst = []
    for i, j in hand:
        num_lst.append(i)

    for i in range(0, 5):
        if num_lst.count(hand[i][0]) == 2:
            g = 1
    if g == 1:
        return True
    else:
        return False


# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+

def evaluate(poker_hand):
    poker_hand.sort()
    print(poker_hand, " is ", end="")
    if royal_flush(poker_hand):
        print("a Royal Flush")
    elif straight_flush(poker_hand):
        print("a Straight Flush")
    elif four_of_a_kind(poker_hand):
        print("a Four of a Kind")
    elif full_house(poker_hand):
        print("a Full House")
    elif flush(poker_hand):
        print("a Flush")
    elif straight(poker_hand):
        print("a Straight")
    elif three_of_a_kind(poker_hand):
        print("Three of a Kind")
    elif two_pair(poker_hand):
        print("Two Pair")
    elif pair(poker_hand):
        print("a Pair")
    else:
        print("Nothing")


# -----------------------------------------+

def main():
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    evaluate([[2, "spd"], [7, "clb"], [8, "dmd"], [A, "dmd"], [Q, "hrt"]])  # nothing
    evaluate([[T, "spd"], [A, "spd"], [Q, "spd"], [K, "spd"], [J, "spd"]])  # royal flush
    evaluate([[T, "clb"], [9, "clb"], [6, "clb"], [7, "clb"], [8, "clb"]])  # straight flush
    evaluate([[2, "dmd"], [7, "clb"], [2, "hrt"], [2, "clb"], [2, "spd"]])  # 4 of a kind
    evaluate([[8, "dmd"], [7, "clb"], [8, "hrt"], [8, "clb"], [7, "spd"]])  # full house
    evaluate([[2, "hrt"], [9, "hrt"], [3, "hrt"], [6, "hrt"], [T, "hrt"]])  # flush
    evaluate([[K, "dmd"], [7, "clb"], [7, "hrt"], [8, "clb"], [7, "spd"]])  # 3 of a kind
    evaluate([[T, "clb"], [9, "clb"], [6, "clb"], [7, "clb"], [8, "spd"]])  # straight
    evaluate([[T, "spd"], [9, "clb"], [6, "dmd"], [9, "dmd"], [6, "hrt"]])  # 2 pair
    evaluate([[T, "spd"], [Q, "clb"], [6, "dmd"], [9, "dmd"], [Q, "hrt"]])  # 1 pair


# -----------------------------------------+

main()
