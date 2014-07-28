class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        else:
            result = 0
            for i in xrange(1, len(prices)):
                if prices[i] - prices[i-1] > 0:
                    result += prices[i] - prices[i-1]
            return result
