class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        result = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                result[i] = result[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                if result[i] <= result[i+1]:
                    result[i] = result[i+1]+1
        return sum(result)
