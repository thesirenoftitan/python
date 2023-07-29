# Create dictionary
calories = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberry": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80",
}


# Get input from user
big_fruit = input("What fruit would you like to check? ")
fruit = big_fruit.casefold()

# Print calories
if fruit in calories:
    number = calories.get(fruit)
    print(number)
else:
    print()