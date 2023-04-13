#237 delete node in linked list
"""
---given a singly linked list, head and want to delete node
---do not have access to head, only node to delete
---return ll with node removed
"""

class Solution:
    def deleteNode(self,node):
        nextNode=node.next.val
        node.val=nodeNext
        node.next=node.next.next

        