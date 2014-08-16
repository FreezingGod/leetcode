# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# this solution use merge sort logK times
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        toremove = []
        for i in range(len(lists)):
            if not lists[i]:
                toremove.append(i)
        toremove.reverse()
        for i in toremove:
            lists.pop(i)
        if not lists: return None
        return self.mergeLists(lists)
    def mergeLists(self, lists):
        if len(lists) == 1:
            return lists[0]
        dummy = ListNode(0)
        head, last = dummy, dummy
        n1, n2 = None, None
        if len(lists) > 2:
            m = len(lists)/2
            n1 = self.mergeLists(lists[0:m])
            n2 = self.mergeLists(lists[m:])
        else:
            n1,n2 = lists[0], lists[1]
        while n1 and n2:
            if n1.val <= n2.val:
                last.next = n1
                last = last.next
                n1 = n1.next
            else:
                last.next = n2
                last = last.next
                n2 = n2.next
        if n1:
            last.next = n1
        else:
            last.next = n2
        return dummy.next
