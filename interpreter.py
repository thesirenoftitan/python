calculation = input("What is your calculation? ")
x, operator, z = calculation.split(" ")

def calculate(x, operator, z):
    x = float(x)
    z = float(z)

    if operator == "+":
        return x + z
    elif operator == "-":
        return x - z
    elif operator == "*":
        return x * z
    elif operator == "/":
        return x / z

print(calculate(x, operator, z))
