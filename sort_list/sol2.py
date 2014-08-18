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
# still TLE, maybe the extra 1 in O(nlogn+1) causing the problem
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if not head or not head.next: return head
        length = self.getLength(head)
        return self.sort(head, length)
    def sort(self, head, length):
        if length <= 1: return head
        m = length / 2
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        while m:
            p1 = p1.next
            m -= 1
        head2 = p1.next
        p1.next = None
        del dummy
        return self.merge(self.sort(head, length/2), self.sort(head2, length-length/2))
    def merge(self, head1, head2):
        if not head1: return head2
        if not head2: return head1
        dummy = ListNode(0)
        last = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                last.next = head1
                head1 = head1.next
            else:
                last.next = head2
                head2 = head2.next
            last = last.next
        if head1: last.next = head1
        if head2: last.next = head2
        return dummy.next
    def getLength(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length

lst = [ListNode(i) for i in [9,8,6,5,4,3,1,2,1,0]]
for i in range(len(lst)-1):
    lst[i].next = lst[i+1]
sol = Solution()
head = sol.sortList(lst[0])
head.p()
