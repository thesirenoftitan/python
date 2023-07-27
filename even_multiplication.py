# ask the user for the multiplication table they want
num = int(input("What multiplication table would you like? "))

# define the size of the multiplication table
table_size = 12

# iterate over the numbers from 1 to table_size
for i in range(1, table_size + 1):
    # calculate the result
    result = i * num
    # check if the result is even
    if result % 2 == 0:
        # formatted print statement
        print(f"{num} x {i:<2} = {result}")
