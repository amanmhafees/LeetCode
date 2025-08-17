# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        current_node=head
        count=0
        while(current_node):
            count+=1
            current_node=current_node.next
        m=count-n
        # print(m)
        if(m==0):
            head=head.next
            return head
        current_node=head
        for i in range(m-1):
            # print(i)
            current_node=current_node.next
        # print(current_node.val)
        current_node.next=current_node.next.next
        return head
            
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        