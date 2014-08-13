# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur.next:
            if cur.val < cur.next.val:
                cur = cur.next
            else:
                pre = dummy
                while pre.next.val < cur.next.val:
                    pre = pre.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
        return dummy.next
