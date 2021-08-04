class Solution:
    def deleteNode(self, node):
        temp=node
        while temp.next.next:
            temp.val=temp.next.val
            temp=temp.next
        temp.val=temp.next.val
        temp.next=None

Your input
[4,5,1,9]
5
Output
[4,1,9]
Expected
[4,1,9]

def deletenode(self,node):
    node.va=node.next.val
    node.next=node.next.next
