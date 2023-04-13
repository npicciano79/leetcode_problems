#lc 148 sort list
"""
---given the head of a linked list
---return the head after sorting in ascending order
"""

class Node:

    def __init__(self,data,n=None,p=None):
        self.data=data
        self.next=n
        self.prev=p
    
    def __str__(self):
        return ('('+str(self.data)+')')

class LinkedList:
    def __init__(self,r=None):
        self.head=r
        self.size=0
    
    def add(self,d):
        new_node=Node(d,self.head)
        self.head=new_node
        self.size+=1

    def printList(self):
        this_node=self.head
        ll_array=[]
        while this_node is not None:
            ll_array.append(this_node.data)
            this_node=this_node.next
        
        return ll_array

    def mergeSortList(self,head):
        
        if not head or not head.next:
            return head
        
        left=head
        right=self.getMiddle(head)
        temp=right.next
        right.next=None
        right=temp

        left=self.mergeSortList(left)
        right=self.mergeSortList(right)

        return self.mergeLeftRight(left,right)


        
    def getMiddle(self,head):
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        return slow

    def mergeLeftRight(self,left,right):
        dummy=tail=Node(-1)
        while left and right:
            if left.data<=right.data:
                tail.next=left
                left=left.next 
            else:
                tail.next=right
                right=right.next
            tail=tail.next 

        tail.next=left if not right else right
        return dummy.next
    





linkedlist=LinkedList()
linkedlist.add(2)
linkedlist.add(1)
linkedlist.add(5)
linkedlist.add(9)
linkedlist.add(12)
linkedlist.add(7)
print(linkedlist.printList())
linkedlist.head=linkedlist.mergeSortList(linkedlist.head)
print(linkedlist.printList())