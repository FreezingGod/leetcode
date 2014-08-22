class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if not s: return ''
        length = len(s)
        isPldm = [[False]*length for _ in range(length)]
        isPldm[-1][-1] = True
        longest = 1
        b,e = 0,0
        for i in range(length-2, -1, -1):
            for j in range(i, length):
                if s[i] == s[j] and (j - i <= 2 or isPldm[i+1][j-1]):
                    isPldm[i][j] = True
                    if j-i+1>longest:
                        longest = j-i+1
                        b,e = i, j+1
        return s[b:e]

s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
sol = Solution()
print sol.longestPalindrome(s)
