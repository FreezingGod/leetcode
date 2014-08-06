class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        smallest = num[-1]
        length = len(num)
        bi = length-1
        si = -1
        bound = si
        for i in range(length-2, bound, -1):
            if num[i] < smallest:
                si = i
                break
            elif num[i] > smallest:
                smallest = num[i]
                bi = i
        if si >= 0:
            for i in range(length-1, bi, -1):
                if num[i] > num[si]:
                    bi = i
                    break
            num[si], num[bi] = num[bi], num[si]
            num[si+1:] = sorted(num[si+1:])
        else:
            num.sort()
        return num

l1 = [1,3,2]
sol = Solution()
print sol.nextPermutation(l1)
