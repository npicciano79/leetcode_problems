#leetcode 86 partition list
"""
---given the head of a linked list and value x
---parition the list for all values less than x and 
---all value greated than x
---must maintain node order
"""
class Node:
    def __init__(self,data,n=None,p=None):
        self.data=data
        self.next=n
        self.prev=p

class LinkedList:
    def __init__(self,r=None):
        self.head=r
        
    def add(self,d):
        new_node=Node(d,self.head)
        self.head=new_node
    
    def printList(self):
        this_node=self.head
        temp_ll=''
        while this_node is not None:
            temp_ll=f" {str(this_node.data)}->{temp_ll}"
            this_node=this_node.next
        
        return temp_ll
        

    def paritionList(self,head,x):

        left=leftDummy=Node(-1)
        right=rightDummy=Node(-1)

        while head:
            if head.data<x:
                left.next=head
                left=left.next
            else:
                right.next=head
                right=right.next
            head=head.next
        left.next=rightDummy.next
        return leftDummy.next


ll=LinkedList()
ll.add(1)
ll.add(4)
ll.add(5)
ll.add(6)
ll.add(2)
print(ll.printList())
ll.paritionList(ll.head,3)
print(ll.printList())