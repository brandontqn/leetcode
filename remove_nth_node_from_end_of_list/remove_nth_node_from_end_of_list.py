# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_indices = []

        # Iterate through entire list, recording each node with it's index
        curr = head
        while curr:
            node_indices.append(curr.val)
            curr = curr.next

        # create and return a new list without the nth-last node
        length = len(node_indices)
        new_head = result = ListNode()
        for idx, val in enumerate(node_indices):
            if idx == length - n:
                continue
            result.next = ListNode(val)
            result = result.next

        return new_head.next