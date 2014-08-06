# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def prt(self):
        p = self
        while p:
            print p.val,
            p = p.next
        print

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        fs = None
        ss = None
        fe = None
        se = None
        f, s = False, False
        p = head
        while p:
            if p.val < x:
                if not f:
                    fs = p
                    fe = p
                    f = True
                else:
                    fe.next = p
                    fe = fe.next
            else:
                if not s:
                    ss = p
                    se = p
                    s = True
                else:
                    se.next = p
                    se = se.next
            p = p.next
        if not f:
            return ss
        else:
            fe.next = ss
            if se:
                se.next = None
            return fs

l = [ListNode(i) for i in [1,4,3,2,5,2]]
for i in range(len(l)-1):
    l[i].next = l[i+1]
sol = Solution()
head = sol.partition(l[0], 3)
head.prt()
