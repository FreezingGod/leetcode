# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next: return head
        dummy = ListNode(0)
        last = head
        pre = dummy
        p = head.next
        duplicate = False
        while p:
            nextp = p.next
            if p.val == last.val:
                duplicate = True
            else:
                if not duplicate:
                    pre.next = last
                    pre = pre.next
                    pre.next = None
                last = p
                duplicate = False
            p = nextp
        if not duplicate:
            pre.next = last
            last.next = None
        return dummy.next
