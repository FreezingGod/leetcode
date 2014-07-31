# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def myprint(self):
        print self.val,
        if self.next:
            self.next.myprint()
        else:
            print

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head:
            return head
        if not head.next:
            return head
        p = head
        prev = None
        root = head.next
        while True:
            pn = p.next
            if not pn:
                break
            p.next = pn.next
            pn.next = p
            if prev:
                prev.next = pn
            prev = p
            p = p.next
            if not p:
                break
        return root

l = [ListNode(i) for i in range(10)]
for i in range(9):
    l[i].next = l[i+1]
sol = Solution()
l[0].myprint()
root = sol.swapPairs(l[0])
root.myprint()
