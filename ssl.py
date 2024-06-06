class Node:
    def __init__(self,n):
        self.data=n
        self.next=None
class sll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbegin(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            self.tail=node
            node.next=None
        else:
            node.next=self.head
            self.head=node
    def insertatend(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            self.tail=node
            node.next=None
        else:
            self.tail.next=node
            self.tail=node
    def delete(self,data):
        temp=self.head
        prev=None
        while(temp.data!=data):
            prev=temp
            temp=temp.next

        prev.next=temp.next
    def insertafter(self,data2,data1):
        node=Node(data1)
        current=self.head
        if self.head==None:
            self.head=node
            self.tail=node
            node.next=None
        else:
            while(current.next!=None):
                current=current.next
                if current.data==data2:
                    break
            node.next=current.next
            current.next=node
    def display(self):
        current=self.head
        while(current.next!=None):
            print(current.data,end='->')
            current=current.next
        print(current.data)
    def reverse(self):
        prev=None
        current=self.head
        nex=None
        while(current.next!=None):
            nex=current.next
            current.next=prev
            prev=current
            current=nex
        nex=current.next
        current.next=prev
        prev=current
        current=nex
        self.tail=self.head
        self.head=prev 
    def length(self):
        count=0
        current=self.head
        while(current!=None):
            count += 1
            current=current.next
        return count
    def rotate(self,k):
        current=self.head
        length=self.length()
        temp=current
        while counter!=0:
            current=current.next
            count -= 1
        temp=current
        current=current.next
        temp.next=None
        while current!=None:
            current.next=self.head
            self.head=current
            


s1=sll()
s1.insertatbegin(int(input()))
s1.insertatbegin(5)
s1.insertatbegin(4)
s1.insertatbegin(int(input()))
s1.insertatbegin(9)
s1.insertatend(80)
s1.insertatend(10)
s1.insertafter(4,7)
s1.delete(69)
s1.display()
a=s1.length()