class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# --
    def get_data(self):
        return self.data
    
    def next_node(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, nextNode):
        self.next = nextNode
# n = Node(56)
# print n.get_data()
# n.set_data(45)
# print n.get_data()

class LinkedList:
    def __init__(self):
        self.head = None
# --
    def is_empty(self):
        return self.head == None

    def add(self,item):
        '''add at head'''
        newNode = Node(item)
        newNode.set_next(self.head)
        self.head = newNode

    def size(self):
        cur = self.head
        count = 0
        while cur != None:
            count+=1
            cur = cur.next_node()
        return count

    def search(self,item):
        cur = self.head
        while cur :
            data = cur.get_data()
            if data == item:
                return data
            else: cur = cur.next_node()
        else: return None

    def remove(self, item):
        cur = self.head
        prev = Node
        found = False
        while not found:
            if cur.get_data() == item:
                found = True
            else:
                prev = cur
                cur = cur.next_node()
        if prev == None:
            self.head = cur.next_node()
        else:
            prev.set_next(cur.next_node())
        return found
            

l = LinkedList()
def add_at_head(k):
    print "** adding nodes at head...**"
    for i in range(k):
        l.add(i)

def allNodes(k):
    n = Node(-1)
    n.set_next(l.head)
    cur = n.next_node()
    for _ in range(k):
        if cur:
            print cur.get_data()
            cur = cur.next_node()
    return "end of nodes"

def getSize():
    return l.size()

def findItem(item):
    msg = "item not available at the moment pls try again later"
    data = l.search(item)
    if data:
        msg = "Found! %s thanks for adding it in the first place :)" %data
    return msg

def delItem(item):
    result = l.remove(4)
    if result:
        print "found! deleted!"
        return allNodes(7)
    
    return "Not Found"


    

add_at_head(7)
print "all nodes: \n",allNodes(7) 
# print "size: ",getSize()
print findItem(5)
print delItem(4)


