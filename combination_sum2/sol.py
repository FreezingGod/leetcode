class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        result = []
        solution = []
        candidates.sort()
        def combine(candidates, target, start):
            if sum(solution) == target:
                result.append(solution[:])
                return
            if sum(solution) > target:
                return
            last = -1
            for i in range(start, len(candidates)):
                if last >= 0 and candidates[i] == candidates[last]:
                    last = i
                    continue
                last = i
                solution.append(candidates[i])
                combine(candidates, target, i+1)
                solution.pop()
        combine(candidates, target, 0)
        return result

A = [10,1,2,7,6,1,5]
t = 8
sol = Solution()
print sol.combinationSum2(A, t)
