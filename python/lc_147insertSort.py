#lc 147 insert sort
"""
---given the head of a singly linked list, sorrt using insertion sort
---return sorted lists head
"""
class Solution(object):
    def insertionSort(self,head):
        sorted=None
        curr=head
        while (curr!=None):
            next=curr.next
            sorted=self.sortInsert(sorted,curr)

            curr=next
        head=sorted
        return head
    
    def sortInsert(self,head_ref,new_node):
        curr=None

        if (head_ref==None or (head_ref.val>=new_node.val)):
            new_node.next=head_ref
            head_ref=new_node
        
        else:
            curr=head_ref
            while (curr.next!=None and curr.next.val<=new_node.val):
                curr=curr.next
            
            new_node.next=curr.next
            curr.next=new_node
        
        return head_ref
    
    def insertionSortItterative(self,head):
        dummy=ListNode(0)
        dummy.next=head
        cur,prev=head.next,head

        while cur:
            if cur.val>=prev.val:
                prev,cur=cur,cur.next
                continue
            tmp=dummy
            while cur.val>tmp.next.val:
                tmp=tmp.next
            prev.next=cur.next
            cur.next=tmp.next
            tmp.next=cur
            cur=prev.next
        return dummy.next
    