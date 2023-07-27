greeting = input("Greeting: \n")

if greeting == 'hello' or greeting == 'Hello' or greeting == ' Hello ' or greeting == 'Hello, Newman':
    print("$0")

elif greeting[0] == 'h' or greeting[0] == 'H':
    print("$20")

else:
    print("$100")