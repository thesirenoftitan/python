class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def view(self):
        return self.stack

stack = Stack()

while True:
    print("\n1.Push\n2.Pop\n3.View\n4.Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        item = input("Enter the item to push: ")
        stack.push(item)
    elif choice == 2:
        item = stack.pop()
        if item:
            print(f"Popped item: {item}")
        else:
            print("Stack is empty.")
    elif choice == 3:
        items = stack.view()
        print(f"Stack: {items}")
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please choose a correct option.")
