class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if not s: return ''
        lst = [1]
        for i in s:
            lst.append(i)
            lst.append(1)
        rad = []
        cc, cm = 0, 0
        longest, lc = 0, 0
        for i in range(len(lst)):
            #print str(cc)+'\t',
            j = 1
            if i < cm:
                mirror = 2*cc-i
                if mirror - rad[mirror]+1 > cc - rad[cc]+1:
                    rad.append(rad[mirror])
                    continue
                else:
                    j = min(rad[mirror], mirror-(cc-rad[cc]))
            while i-j >= 0 and i+j < len(lst) and lst[i-j] == lst[i+j]:
                j+=1
            rad.append(j)
            if i+j-1 > cm:
                cm = i+j-1
                cc = i
            if j-1 > longest:
                longest = j-1
                lc = i
        #print
        #for i in range(len(lst)):
        #    print str(i)+'\t',
        #print
        #for i in lst:
        #    print str(i)+'\t',
        #print
        #for i in rad:
        #    print str(i)+'\t',
        #print
        result = ''
        for i in range(lc-longest+1, lc+longest):
            if lst[i] != 1:
                result = result + lst[i]
        return result

s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
sol = Solution()
print sol.longestPalindrome(s)
