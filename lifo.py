from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.popleft()

    def view(self):
        return list(self.queue)

queue = Queue()

while True:
    print("\n1.Enqueue\n2.Dequeue\n3.View\n4.Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        item = input("Enter the item to enqueue: ")
        queue.enqueue(item)
    elif choice == 2:
        item = queue.dequeue()
        if item:
            print(f"Dequeued item: {item}")
        else:
            print("Queue is empty.")
    elif choice == 3:
        items = queue.view()
        print(f"Queue: {items}")
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please choose a correct option.")
