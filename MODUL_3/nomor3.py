class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class LinkedList: 
    def __init__(self): 
        self.head = None
    def pushAw(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
    def pushAk(self, data):
        if (self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
    def insert(self,data,pos):
        node = Node(data)
        if not self.head:
            self.head = node
        elif pos==0:
            node.next = self.head
            self.head = node
        else:
            prev = None
            current = self.head
            current_pos = 0
            while(current_pos < pos) and current.next:
                prev = current
                current = current.next
                current_pos +=1
            prev.next = node
            node.next = current
        return self.head
    def deleteNode(self, position): 
        if self.head == None: 
            return 
        temp = self.head 
        if position == 0: 
            self.head = temp.next
            temp = None
            return 
        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break
        if temp is None: 
            return 
        if temp.next is None: 
            return 
        next = temp.next.next
        temp.next = None
        temp.next = next 
    def search(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return "True"
            current = current.next
        return "False"
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next

list1 = LinkedList() 
list1.pushAw(30)
list1.pushAw(27)
list1.pushAw(39)
list1.pushAw(56)
list1.pushAw(9)
list1.pushAw(17)
list1.pushAk(3)
list1.deleteNode(0)
list1.insert(8,5)
print(list1.search(30))
print(list1.search(12))
list1.display()
