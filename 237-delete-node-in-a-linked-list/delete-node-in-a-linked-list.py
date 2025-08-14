# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        # current_node=self.head
        # while(current_node!=None):
        #     if(current_node.data==node):
        #         prev.next=current_node.next
        #         return 0;
        #     prev=cuurent_node
        #     current_node=current_node.next
        node.val = node.next.val
        node.next = node.next.next

        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        