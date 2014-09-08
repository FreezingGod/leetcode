# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                while True:
                    if fast == slow: # check first to output the correct answer for which the whole list is a cycle
                        return fast
                    fast = fast.next
                    slow = slow.next
        return None
