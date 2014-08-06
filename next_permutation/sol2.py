class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        length = len(num)
        fi = -1
        for i in range(length-1, 0, -1):
            if num[i-1] < num[i]:
                fi = i-1
                break
        bi = length-1
        if fi >= 0:
            for i in range(length-1, fi, -1):
                if num[i] > num[fi]:
                    bi = i
                    break
            num[fi],num[bi] = num[bi],num[fi]
        fi = fi+1; bi = length-1
        while fi < bi:
            num[fi],num[bi] = num[bi], num[fi]
            fi += 1
            bi -= 1
        return num

l1 = [1,2,3]
l2 = [3,2,1]
l3 = [1,1,5]
l4 = [1,2]
l5 = [1,3,2]
sol = Solution()
print sol.nextPermutation(l1)
print sol.nextPermutation(l2)
print sol.nextPermutation(l3)
print sol.nextPermutation(l4)
print sol.nextPermutation(l5)
