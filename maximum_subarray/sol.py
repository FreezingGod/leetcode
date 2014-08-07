class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        maxsum = -10e9
        sum = 0
        for i in range(len(A)):
            sum += A[i]
            if sum > maxsum:
                maxsum = sum
            if sum < 0:
                sum = 0
        return maxsum
