# this solution got time limit exceeded
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        return self.dfs(S,T)
    def dfs(self, S, T):
        if T == '':
            return 1
        if S == '':
            return 0
        for i in range(len(S)):
            if S[i] == T[0]:
                n1 = self.dfs(S[i+1:], T)
                n2 = self.dfs(S[i+1:], T[1:])
                return n1 + n2
        return 0

S = 'rrabbbbit'
T = 'rabbit'
S,T = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe", "bddabdcae"
S = 'rrarabbbit'
T = 'rabbit'
sol = Solution()
print sol.numDistinct(S,T)
