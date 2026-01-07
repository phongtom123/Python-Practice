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

    def insert_head(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node


    def insert_after(self, key, data):
        cur = self.head
        while cur:
            if cur.data == key:
                new_node = Node(data)
                new_node.next = cur.next
                cur.next = new_node
                return
            cur = cur.next
        print("Không tìm thấy node")

# ll = Linked_list()
# ll.append(10)
# ll.append(20)
# ll.append(30)
# ll.append(20)
# ll.append(30)
# ll.delete(30)
# ll.delete(30)
# ll.push(291)
# ll.display()
# ll.insert_after(291,1)

a=None
b=Linked_list()
c=None
count=1
while (True):
    n = int(input("Nhập lựa chọn: \n" \
    "1. Thêm node\n" \
    "2. Xóa node\n" \
    "3. Nhập giá trị của vị trí node muốn thêm\n" \
    "4. Displays\n"))

    match n:
        case 1:
            while True:
                a = str(input(f"Nhập giá trị node {count}: "))
                if a == "-1":
                    break
                b.append(a)
                count+=1

        case 2:
            a = str(input(f"Nhập giá trị muốn xóa: "))
            b.delete(a)
            b.display()
        
        case 3:
            a = str(input(f"Nhập giá trị muốn thêm: "))
            c = str(input(f"Nhập node muốn thêm sau: "))
            b.insert_after(c,a)
        case 4:
            if a != None:
                b.display()
            else:
                print("Danh sách trống")

        case -1:
            break