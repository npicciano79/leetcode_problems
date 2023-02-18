#92 reverse linked list 2
"""
---given the head of a singly linked list and 
---two integers, right and left where left<=right
---reverse the nodes of the list from position left to right 
---return reversed list
"""

class Solution(object):
    def reverseBetween(self,head,left,right):
        #empty linked list
        if not head:
            return None 

        #initalize cur and prev pointers 
        cur,prev=head,None

        #position cur at left and prev 1 before cur
        while left: 
            prev=cur
            cur=cur.next
            left,right=left-1,right-1

        #set con and tail pointers 
        con=prev
        tail=cur

        #reverse nodes between left and right pointers 
        while right:
            third=cur.next 
            cur.next=prev 
            prev=cur
            cur=third 
            right-=1 

        #connect reversed nodes to original values 
        if con:
            con.next=prev 
        else:
            head=prev
        tail.next=cur

        return head 




        