# still time limit exceeded
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        mm = {}
        for c in T:
            if c not in mm:
                mm[c] = []
                for i in range(len(S)):
                    if S[i] == c:
                        mm[c].append(i)
        return self.countNum(mm, S, T, 0, len(S)-1)
    def countNum(self, mm, S, T, b, e): # count number of occurrance of T in S[b:e+1]
        #print S[b:e+1], T
        if T == '':
            return 1
        if b > e:
            return 0
        if len(T) == 1:
            return self.bisearch(mm, T[0], b, e)
        m = len(T)/2
        result = 0
        for idx in mm[T[m]]:
            if idx >=b and idx <= e:
                n1 = self.countNum(mm, S, T[0:m], b, idx-1)
                #print '\t',S[b:idx], T[0:m], n1
                n2 = self.countNum(mm,S, T[m+1:], idx+1, e)
                #print '\t',S[idx+1:], T[m+1:], n2
                result += n1*n2
        return result
    def bisearch(self, mm, c, b, e):
        lst = mm[c]
        if not lst: return 0
        length = len(lst)
        i1, i2 = -1, -1
        if e < lst[0] or b > lst[-1]:
            return 0
        if b <= lst[0]:
            i1 = 0
        else:
            start,end = 0, length-1
            while start <= end:
                m = (start+end)/2
                if lst[m] == b:
                    i1 = m
                    break
                elif lst[m] < b:
                    if m+1 < length and lst[m+1] >= b:
                        i1 = m+1
                        break
                    else:
                        start = m+1
                else:
                    if m-1 >= 0 and lst[m-1] < b:
                        i1 = m
                        break
                    else:
                        end = m-1
        if e >= lst[-1]:
            i2 = length-1
        else:
            start,end = 0, length-1
            while start <= end:
                m = (start+end)/2
                if lst[m] == e:
                    i2 = m
                    break
                elif lst[m] < e:
                    if m+1 < length and lst[m+1] >= e:
                        i2 = m+1
                        break
                    else:
                        start = m+1
                else:
                    if m-1 >= 0 and lst[m-1] < e:
                        i1 = m
                        break
                    else:
                        end = m-1
        return i2 - i1 + 1
S,T = "xslledayhxhadmctrliaxqpokyezcfhzaskeykchkmhpyjipxtsuljkwkovmvelvwxzwieeuqnjozrfwmzsylcwvsthnxujvrkszqwtglewkycikdaiocglwzukwovsghkhyidevhbgffoqkpabthmqihcfxxzdejletqjoxmwftlxfcxgxgvpperwbqvhxgsbbkmphyomtbjzdjhcrcsggleiczpbfjcgtpycpmrjnckslrwduqlccqmgrdhxolfjafmsrfdghnatexyanldrdpxvvgujsztuffoymrfteholgonuaqndinadtumnuhkboyzaqguwqijwxxszngextfcozpetyownmyneehdwqmtpjloztswmzzdzqhuoxrblppqvyvsqhnhryvqsqogpnlqfulurexdtovqpqkfxxnqykgscxaskmksivoazlducanrqxynxlgvwonalpsyddqmaemcrrwvrjmjjnygyebwtqxehrclwsxzylbqexnxjcgspeynlbmetlkacnnbhmaizbadynajpibepbuacggxrqavfnwpcwxbzxfymhjcslghmajrirqzjqxpgtgisfjreqrqabssobbadmtmdknmakdigjqyqcruujlwmfoagrckdwyiglviyyrekjealvvigiesnvuumxgsveadrxlpwetioxibtdjblowblqvzpbrmhupyrdophjxvhgzclidzybajuxllacyhyphssvhcffxonysahvzhzbttyeeyiefhunbokiqrpqfcoxdxvefugapeevdoakxwzykmhbdytjbhigffkmbqmqxsoaiomgmmgwapzdosorcxxhejvgajyzdmzlcntqbapbpofdjtulstuzdrffafedufqwsknumcxbschdybosxkrabyfdejgyozwillcxpcaiehlelczioskqtptzaczobvyojdlyflilvwqgyrqmjaeepydrcchfyftjighntqzoo", "rwmimatmhydhbujebqehjprrwfkoebcxxqfktayaaeheys"
sol = Solution()
print sol.numDistinct(S,T)
