# Definition for singly-linked list.
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
        if m == n: return head
        head1 = head
        tail1 = head
        for i in range(1, m-1):
            tail1 = tail1.next
        if m == 1:
            head2 = head
        else:
            head2 = tail1.next
        tail2 = head2
        nn = head2.next
        head3 = None
        for i in range(n-m):
            tmp = nn
            nn = nn.next
            tmp.next = head2
            head2 = tmp
        head3 = nn
        if m == 1:
            head1 = head2
        else:
            tail1.next = head2
        tail2.next = head3
        return head1
lst = []
for i in range(1,6):
    lst.append(ListNode(i))
for i in range(4):
    lst[i].next = lst[i+1]
lst[0].p()
sol = Solution()
root = sol.reverseBetween(lst[0], 1,5)
root.p()
