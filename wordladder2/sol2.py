import string
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        dict.add(end)
        current, previous = [], []
        premap = {start:None}
        current.append(start)
        while dict:
            previous = current
            current = []
            toremove = set()
            found = False
            for word in previous:
                for i in range(len(word)):
                    for c in string.lowercase:
                        neww = word[:i] + c + word[i+1:]
                        if c != word[i] and neww in dict:
                            current.append(neww)
                            toremove.add(neww)
                            premap[neww] = premap.get(neww, [])
                            premap[neww].append(word)
                            if neww == end:
                                found = True
            for w in toremove:
                dict.remove(w)
            if found:
                break
            if not current:
                return []
        print premap
        return self.buildPath(start, end, premap)
    def buildPath(self, start, end, premap):
        result = []
        current = [end]
        def dfs(start, current):
            if current[-1] == start:
                result.append(current[::-1])
                return
            for w in premap[current[-1]]:
                current.append(w)
                dfs(start, current)
                current.pop()
        dfs(start, current)
        return result

sol = Solution()
print sol.findLadders("a", "c", set(["a", "b", "c"]))
