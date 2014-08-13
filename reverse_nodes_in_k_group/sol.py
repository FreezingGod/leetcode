# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def p(self):
        print self.val,
        if self.next:
            self.next.p()
        else:
            print

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if not head or not head.next: return head
        if k <= 1: return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        last = dummy
        while cur:
            c = k - 1
            ch = cur
            while c > 0 and cur:
                cur = cur.next
                c -= 1
            if not cur:
                last.next = ch
                break
            cn = cur.next
            pre = None
            clast = ch
            c = k
            for i in range(k):
                tmp = ch.next
                ch.next = pre
                pre = ch
                ch = tmp
            last.next = pre
            last = clast
            cur = cn
        return dummy.next
lst = [ListNode(i) for i in range(1, 6)]
for i in range(len(lst)-1):
    lst[i].next = lst[i+1]
sol = Solution()
lst[0].p()
h = sol.reverseKGroup(lst[0], 5)
h.p()
