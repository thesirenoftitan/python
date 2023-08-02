try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    assert num1 != 0 and num2 != 0, "Neither number can be zero!"

    if num1 > num2:
        if num1 % num2 == 0:
            print(num1, "is a multiple of", num2)
        else:
            print(num1, "is not a multiple of", num2)
    else:
        if num2 % num1 == 0:
            print(num2, "is a multiple of", num1)
        else:
            print(num2, "is not a multiple of", num1)
except ValueError:
    print("That is not an integer!")
except AssertionError as e:
    print(e)  # Prints the error message associated with the assertion
