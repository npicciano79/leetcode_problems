#328 odd even linked list 
"""
---given the head of a linked list
---group all nodes with even indices and odd indices
---first node is odd, secodn is even
---solve in O(n) time complexity
"""

class Solution (object):
    def oddEvenList(self,head):
        
        #check for empty list
        if not head or not head.next:
            return head

        #position pointers
        cur=head.next
        prev=head
        future=cur.next
        tail=cur 

        #connect even and odd nodes
        while future:
            prev.next=future
            cur.next=future.next
            prev=future
            cur=future.next
            if cur:
                future=cur.next
            else:
                future=cur

        #connect sorted notes to beginning of list
        prev.next=tail 

        return head 
        

