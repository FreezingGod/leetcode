class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        nums = list(set(candidates))
        nums.sort()
        result, current = [], []
        self.dfs(result, current, 0, nums, target)
        return result
    def dfs(self, result, current, cursum, candidates, target):
        if cursum == target:
            result.append(current[:])
            return
        for i in candidates:
            if cursum + i <= target:
                current.append(i)
                self.dfs(result, current, cursum+i, candidates, target)
                current.pop()
            else:
                break

sol = Solution()
print sol.combinationSum([2,3,6,7], 7)
