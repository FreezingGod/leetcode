import copy
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        result = []
        sample = []
        visited = [0] * len(num)
        if len(num) == 0:
            return []
        else:
            self.mypermute(result, sample, visited, num)
            return result
    def mypermute(self, result, sample, visited, num):
        if len(sample) == len(num):
            result.append(copy.deepcopy(sample))
        for i in range(len(num)):
            if not visited[i]:
                visited[i] = 1
                sample.append(num[i])
                self.mypermute(result, sample, visited, num)
                visited[i] = 0
                sample.pop()

num = [1,2,3]
sol = Solution()
print sol.permute(num)
