def main():
    name = camel_case()
    print(snake_case(name))

# take input
def camel_case():
    name = input("What is the name?\n")
    return name

# change to snake case
def snake_case(name):
    new_name = ""
    for character in name:
        # check to see if it's uppercase
        if character.isupper():
        # if so then replace whitespace with underscore
            new_name += "_" + character.lower()
        else:
            new_name += character
    return new_name.lstrip("_")




main()