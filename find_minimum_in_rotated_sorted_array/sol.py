class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num) == 1: return num[0]
        if len(num) == 2: return min(num[0], num[1])
        mid = len(num)/2
        if num[0] < num[mid]:
            return min(num[0], self.findMin(num[mid+1:]))
        else:
            return self.findMin(num[:mid+1])
