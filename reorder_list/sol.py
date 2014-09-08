# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head: return head
        length = 1
        cur = head
        while cur:
            cur = cur.next
            length += 1
        mid = (length+1)/2
        cur = head
        for i in range(mid-1):
            cur = cur.next
        eol1 = cur
        eol2 = cur.next
        eol1.next = None
        dummy = ListNode(0)
        cur = eol2
        while cur:
            n = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = n
        p2 = dummy.next
        p1 = head
        while p1:
            np1 = p1.next
            if p2:
                np2 = p2.next
                p1.next = p2
                p2.next = np1
                p2 = np2
            p1 = np1
        return head
