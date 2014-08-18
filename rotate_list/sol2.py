# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or not head.next: return head
        p = head
        length = 0
        last = None
        while p:
            length += 1
            p = p.next
            if p and p.next == None:
                last = p
        k = k % length
        if k == 0:
            return head
        n = length-k-1
        last.next = head
        p = head
        while n:
            n -= 1
            p = p.next
        tmp = p.next
        p.next = None
        return tmp

