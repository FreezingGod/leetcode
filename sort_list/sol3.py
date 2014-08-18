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

# still TLE, I'm pissed!!
# I had tried a few solutions on the web who claims to had passed the Judge, but I always get TLE
# guess there is something wrong with the time limit on the judge
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if not head or not head.next: return head
        return self.sort(head)
    def sort(self, head):
        if not head or not head.next: return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        return self.merge(self.sort(head), self.sort(head2))
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

lst = [ListNode(i) for i in [9,8,6,5,4,3,1,2,1,0]]
for i in range(len(lst)-1):
    lst[i].next = lst[i+1]
sol = Solution()
head = sol.sortList(lst[0])
head.p()
