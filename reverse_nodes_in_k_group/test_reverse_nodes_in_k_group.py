import unittest
import reverse_nodes_in_k_group

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TestReverseKGroup(unittest.TestCase):
    def test_1(self):
        k = 2
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        sol = reverse_nodes_in_k_group.Solution()
        res = sol.reverseKGroup(head, k)
        arr = []
        while res:
            arr.append(res.val)
            res = res.next
        self.assertEqual(arr, [2, 1, 4, 3, 5])

if __name__ == '__main__':
    unittest.main()