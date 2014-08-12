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
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if not head or m == n: return head
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        for i in range(1, m):
            p = p.next
        start = p.next
        while m < n:
            tmp = start.next
            start.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            m +=1
        return dummy.next
lst = []
for i in range(1,6):
    lst.append(ListNode(i))
for i in range(4):
    lst[i].next = lst[i+1]
lst[0].p()
sol = Solution()
root = sol.reverseBetween(lst[0], 2,4)
root.p()
