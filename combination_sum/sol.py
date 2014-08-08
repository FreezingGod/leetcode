class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        result = []
        current = []
        candidates.sort()
        def combine(candidates, t, start):
            if sum(current) == t:
                tmp = current[:]
                result.append(tmp)
            elif sum(current) > t:
                return
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                combine(candidates, t, i)
                current.pop()
        combine(candidates, target,0)
        return result

sol = Solution()
c = [2,6, 7,3]
t = 7
print sol.combinationSum(c,t)
