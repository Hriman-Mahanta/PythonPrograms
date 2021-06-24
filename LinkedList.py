# 31. Program to create a linked list.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def add_at_beg(self,new_data):
        new_node=Node(new_data)
        if self.head==None:
            new_node.next=None
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def add_at_end(self,new_data):
        new_node=Node(new_data)
        if self.head==None:
            new_node.next=None
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.next=None
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next

lList=LinkedList()
lList.add_at_beg(1)
lList.add_at_beg(5)
lList.add_at_end(7)
lList.add_at_end(3)
lList.add_at_beg(9)
lList.display()