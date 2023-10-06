# --------------------------------------
# CSCI 127, Lab 8                      |
# Month 10, 2021                       |
# Ben Farrell                          |
# switching from first to third person pov |
# --------------------------------------

# while loop checks that there hasn't been values assigned to friend_pronouns parameter and then proceeds asking for the input

dic_m = {' me': ' him', 'myself': 'himself', 'i ': 'he ', ' am': ' is', "i'm": "he's", ' my': ' his', ' have': ' has',
         'want': 'wants'}
dic_f = {' me': ' her', 'myself': 'herself', 'i ': 'she ', ' am': ' is', "i'm": "she's", ' my': ' her', ' have': ' has',
         'want': 'wants'}
dic_p = {' me': ' them', 'myself': 'themselves', 'i ': 'they ', ' am': ' are', "i'm": "they're", ' my': " their"}


def first2third(user_string, friend_pronouns):
    user_string = user_string.lower()
    if friend_pronouns == 'm':
        for k, v in dic_m.items():
            user_string = user_string.replace(k, v)
        return user_string
    if friend_pronouns == 'f':
        for k, v in dic_f.items():
            user_string = user_string.replace(k, v)
        return user_string
    if friend_pronouns == 'p':
        for k, v in dic_p.items():
            user_string = user_string.replace(k, v)
        return user_string


def main():
    user_string = input("Enter the question to be translated: ")
    friend_name = input("Enter the name of the friend: ")
    print(friend_name + "'s pronouns: masculine, feminine, or plural/neutral?  ")
    friend_pronouns = ""
    while (friend_pronouns != 'm' and friend_pronouns != 'f' and friend_pronouns != 'p'):
        friend_pronouns = input("Enter m, f, or p: ").lower()
    translation = first2third(user_string, friend_pronouns)
    print('Asking for a friend, ' + friend_name + '...')
    print(translation)


main()
