class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:
            return True
        s = s.lower()
        p1, p2 = 0, len(s)-1
        while p1 < p2:
            while not s[p1].isalnum() and p1 < len(s)-1:
                p1 += 1
            while not s[p2].isalnum() and p2 > 0:
                p2 -= 1
            if s[p1].isalnum() and s[p2].isalnum():
                if not s[p1] == s[p2]:
                    return False
                else:
                    p1 += 1
                    p2 -= 1
        return True

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = "1a2"
s4 = ".a"
sol = Solution()
print sol.isPalindrome(s1)
print sol.isPalindrome(s2)
print sol.isPalindrome(s3)
print sol.isPalindrome(s4)
