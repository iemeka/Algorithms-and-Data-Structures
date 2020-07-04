class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def peek_item(self,pos):
        return self.items[pos]

    def size(self):
        return len(self.items)

q = Queue()
