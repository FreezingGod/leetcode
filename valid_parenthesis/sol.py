class Solution:
    # @return a boolean
    def isValid(self, s):
        openset = set(['(', '{', '['])
        map = dict()
        map['('] = ')'
        map['{'] = '}'
        map['['] = ']'
        stack = []
        result = True
        for i in s:
            if i in openset:
                stack.append(map[i])
            else:
                if not stack:
                    result = False
                    break
                elif not stack.pop() == i:
                    result = False
                    break
        if stack:
            result = False
        return result
