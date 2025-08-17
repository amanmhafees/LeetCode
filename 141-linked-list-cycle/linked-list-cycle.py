# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        # myset=set()
        # curr=head
        # while(curr):
        #     if(curr in myset):
        #         return True
        #     myset.add(curr)
        #     curr=curr.next
        # return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:   # they meet => cycle
                return True
        return False
        """
        :type head: ListNode
        :rtype: bool
        """
        