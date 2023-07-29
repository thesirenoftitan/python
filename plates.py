def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Check if length of plate is less than 2 or more than 6
    if len(plate) < 2 or len(plate) > 6:
        return False

    # Check if the first two characters of plate are not letters
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False

    # Check if any character after the first two is not a letter or number
    for character in plate[2:]:
        if not character.isalnum():
            return False

    # Check if the first number in the plate is 0
    for character in plate[2:]:
        if character.isdigit():
            if character == '0':
                return False
            break  # Exit the loop as soon as the first number is found

    # Check if any characters after a number is a letter
    found_digit = False
    for character in plate[2:]:
        if character.isdigit():
            found_digit = True
        elif found_digit and character.isalpha():
            return False

    return True


main()