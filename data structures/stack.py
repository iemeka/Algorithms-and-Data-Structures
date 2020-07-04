class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add(self,item):
        self.items.append(item)

    def remove(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

s = Stack()


