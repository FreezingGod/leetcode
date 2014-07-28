class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        maxProfit, minPoint = 0, 0
        bb, bs = 0, 0
        for i in xrange(len(prices)):
            if prices[i] < prices[minPoint]:
                minPoint = i
            elif prices[i] - prices[minPoint] > maxProfit:
                maxProfit = prices[i] - prices[minPoint]
                bb = minPoint
                bs = i
        return maxProfit
