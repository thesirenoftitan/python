def main():
    tweet = get_tweet()
    new_string(tweet)

def get_tweet():
    tweet = input("Input: ")
    return tweet

def new_string(tweet):
    new_str = ""
    for character in tweet:
        if character.lower() not in ["a", "e", "i", "o", "u"]:
            new_str += character
    print(new_str)

main()
