class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        result = []
        current = []
        self.add(s, 0, len(s)-1, result, current)
        return result
    def add(self, s, start, end, result, current):
        if start > end:
            result.append(current[:])
            return
        if start == end:
            current.append(s[start])
            result.append(current[:])
            current.pop()
            return
        for i in range(start, end+1):
            if self.isPalindrome(s, start, i):
                current.append(s[start:i+1])
                self.add(s, i+1, end, result, current)
                current.pop()
    def isPalindrome(self, s, b, e):
        while b <= e:
            if s[b] == s[e]:
                b += 1
                e -= 1
            else:
                return False
        return True

s = 'aa'
sol = Solution()
print sol.partition(s)
