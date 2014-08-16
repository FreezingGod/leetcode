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
        # head sort, maintain a min-heap
        heapsize = len(lists)
        dummy = ListNode(0)
        last = dummy
        self.buildHeap(lists)
        while lists:
            last.next = lists[0]
            last = last.next
            lists[0] = lists[0].next
            if not lists[0]:
                lists[0], lists[-1] = lists[-1], lists[0]
                lists.pop()
                self.minHeapify(lists, len(lists), 0)
            else:
                self.minHeapify(lists, len(lists), 0)
        return dummy.next
    def minHeapify(self, lists, heapsize, i):
        i += 1 # 1 based index system
        l,r,smallest = i*2, i*2+1, i
        if l <= heapsize:
            smallest = i if lists[i-1].val <= lists[l-1].val else l
        if r <= heapsize:
            smallest = smallest if lists[smallest-1].val <= lists[r-1].val else r
        if smallest != i:
            lists[smallest-1], lists[i-1] = lists[i-1], lists[smallest-1]
            self.minHeapify(lists, heapsize, smallest-1)
    def buildHeap(self, lists):
        heapsize = len(lists)
        for i in range(heapsize/2, -1, -1):
            self.minHeapify(lists, heapsize, i)
