class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        if not words: return []
        if L <= 0: return words
        result = []
        s,i = 0, 0
        while i < len(words):
            s = i
            l1, l2, count = 0, 0, 0
            while i < len(words) and l1+len(words[i]) < L:
                l1 += len(words[i])+1
                l2 += len(words[i])
                count += 1
                i += 1
            if i < len(words) and l1 + len(words[i]) == L:
                l1 += len(words[i])
                l2 += len(words[i])
                count += 1
                i += 1
            if count == 1:
                result.append(words[s] + ' '*(L-l2))
            else:
                if i < len(words):
                    width = (L-l2)/(count-1)
                    leading = L-l2-(count-1)*width
                    sentence = ''
                    for j in range(s, i-1):
                        sentence = sentence + words[j] + ' '*(width+1 if j-s < leading else width)
                    sentence = sentence + words[i-1]
                    result.append(sentence)
                else:
                    sentence = ''
                    for j in range(s, i-1):
                        sentence = sentence + words[j] + ' '
                    sentence = sentence + words[i-1] + ' '*(L-l2-count+1)
                    result.append(sentence)
        return result
#words = ["This", "is", "an", "example", "of", "text", "justification."]
words = ["What","must","be","shall","be."]
sol = Solution()
print sol.fullJustify(words, 12)
