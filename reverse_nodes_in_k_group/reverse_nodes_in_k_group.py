# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Given a linked list, reverse the nodes of a linked list k at a time 
# and return its modified list. k is a positive integer and is less 
# than or equal to the length of the linked list. If the number of 
# nodes is not a multiple of k then left-out nodes in the end should 
# remain as it is.

# Example:
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        # get group of k nodes
        k_group = self.getKGroup(curr, k)
        prev = None
        # check if group contains all valid nodes, loop
        while len(k_group) == k:
            # reverse
            curr = self.reverseLinkedList(k_group[0], prev, k)
            k_group = self.getKGroup(curr, k)

        return head

    # returns a k-length grouping
    def getKGroup(self, start: ListNode, k: int) -> [int]:
        result = []
        curr = start
        for _ in range(k):
            if curr == None:
                break
            result.append(curr)
            curr = curr.next
        return result

    # returns the head of reversed k-group
    def reverseLinkedList(self, start: ListNode, start_prev: ListNode, k: int):
        prev = None
        curr = start
        next = None
        
        i = 0
        while i < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1

        return curr