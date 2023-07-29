def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Check if length of plate is less than 2 or more than 6
    if length of plate < 2 or length of plate > 6:
        return False

    # Check if the first two characters of plate are not letters
    if first character of plate is not a letter or second character of plate is not a letter:
        return False

    # Check if any character in plate from the third position to the end is a number
    for every character in plate from third position to the end:
        if character is a number:
            return False

    # Check if any character in plate is not a letter or number
    for every character in plate:
        if character is not a letter and character is not a number:
            return False

    # If the plate passed all checks, it is valid
    return True




main()