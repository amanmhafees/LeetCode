# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self,head):
        prev=None
        curr=head
        while(curr):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second_half=self.reverse(slow)#slow will be pointing to the middle of linked list
        
        first,second=head,second_half
        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True
        
        
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        