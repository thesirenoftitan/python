# Multiplication table 

num = 12

# User input

num = int(input("What multiplication table would you like?"))

# iterate 12 times from i = 1 to 12
for i in range(1,13):
    print(num, 'x', i, '=', num*i)