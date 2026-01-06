class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, "->", end=" ")
            cur = cur.next
        print("None")
    
    def delete(self, key):
        cur = self.head

        if cur and cur.data == key:
            self.head = cur.next
            return

        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next

        if cur:
            prev.next = cur.next

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node



ll = Linked_list()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(20)
ll.append(30)
ll.delete(30)
ll.delete(30)
ll.push(291)
ll.display()
