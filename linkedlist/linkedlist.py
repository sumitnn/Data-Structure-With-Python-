class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def showlist(self):
        a = self.head
        while a is not None:
            print(a.data)
            a = a.next

    def revshowlist(self):
        pass

    def pushb(self, x):  # at begining
        newnode = Node(x)
        newnode.next = self.head
        self.head = newnode

    def pushe(self, x):
        newnode = Node(x)
        a = self.head.next
        while a is not None:
            if a.next == None:
                a.next = newnode
                break

            a = a.next


s = LinkedList()
s.head = Node(10)
e2 = Node(20)
e3 = Node(30)
s.head.next = e2
e2.next = e3
# s.showlist()
s.pushb(5)
s.showlist()
s.pushe(50)
s.pushe(100)
s.showlist()
