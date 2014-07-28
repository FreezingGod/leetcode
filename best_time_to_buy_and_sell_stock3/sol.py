class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        forward = []
        backward = []
        maxProfit, minPoint = 0, 0
        for i in range(len(prices)):
            if prices[i] < prices[minPoint]:
                minPoint = i
            elif prices[i] - prices[minPoint] > maxProfit:
                maxProfit = prices[i] - prices[minPoint]
            forward.append(maxProfit)
        iters = range(len(prices))
        iters.reverse()
        maxProfit, maxPoint = 0, len(prices)-1
        for i in iters:
            if prices[i] > prices[maxPoint]:
                maxPoint = i
            elif prices[maxPoint] - prices[i] > maxProfit:
                maxProfit = prices[maxPoint] - prices[i]
            backward.append(maxProfit)
        backward.reverse()
        m = forward[0] + backward[0]
        for i in range(len(prices)):
            if forward[i] + backward[i] > m:
                m = forward[i] + backward[i]
        return m
prices = [1,2]
sol = Solution()
print sol.maxProfit(prices)
