#61 rotate list
"""
---given the head of a linked list
---rotate the list to the right by k places
---runtime: 33ms memory: 13.6mb
"""



class Solution(object):
    def rotateRight(self,head,k):
        if head and head.next:
            temp_head=head
            count=0
            while temp_head:
                temp_head=temp_head.next
                count+=1
            if k>count:
                k=k%count
            
            while k:
                next_val=head
                last=next_val.next
                while last.next:
                    last=last.next
                    next_val=next_val.next
                next_val.next=last.next
                last.next=head
                head=last
                k-=1
        return head 