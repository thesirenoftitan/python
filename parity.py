def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("That's an even number!")
    else:
        print("That's an odd number!")

def is_even(n):
    return n % 2 == 0

main()