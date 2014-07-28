class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        def buildPath(path, word):
            if len(prevMap[word]) == 0:
                path.append(word)
                p = path[:]
                p.reverse()
                result.append(p)
                path.pop()
                return
            path.append(word)
            for w in prevMap[word]:
                buildPath(path, w)
            path.pop()

        length = len(start)
        prevMap = {}
        dict.add(start)
        dict.add(end)
        for w in dict:
            prevMap[w] = []
        result = []
        candidates = [set(), set()]
        current, previous = 0, 1
        candidates[current].add(start)
        while True:
            current, previous = previous, current
            for w in candidates[previous]:
                dict.remove(w)
                candidates[current].clear()
            for w in candidates[previous]:
                for i in xrange(length):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if j != w[i]:
                            neww = w[0:i] + j + w[i+1:]
                            if neww in dict:
                                candidates[current].add(neww)
                                prevMap[neww].append(w)
            if not candidates[current]: return result
            if end in candidates[current]: break
        buildPath([], end)
        return result
start = "hit"
end = "cog"
dict = set(["hot","dot","dog","lot","log"])
sol = Solution()
print sol.findLadders(start, end, dict)
