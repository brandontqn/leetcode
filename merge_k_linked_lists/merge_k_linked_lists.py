# https://leetcode.com/problems/merge-k-sorted-lists/

# Given an array of linked-lists lists, each linked list is sorted in ascending order.
# Merge all the linked-lists into one sort linked-list and return it.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        total_length = len(lists)
        interval = 1
        while interval < total_length:
            for i in range(0, total_length - interval, interval * 2):
                lists[i] = self.merge(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if total_length > 0 else None

    def merge(self, list_1: ListNode, list_2: ListNode):
        head = point = ListNode(0)
        while list_1 and list_2:
            if list_1.val <= list_2.val:
                point.next = list_1
                list_1 = list_1.next
            else:
                point.next = list_2
                list_2 = list_2.next
            point = point.next
        if not list_1:
            point.next = list_2
        else:
            point.next = list_1
        return head.next