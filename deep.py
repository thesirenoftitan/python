answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? \n").strip().lower()

# if answer is equal to 42, forty two, forty-two then print yes
if answer == '42' or answer == 'forty two' or answer == 'forty-two':
    print("Yes")

# if not, print no
else:
    print("No")
