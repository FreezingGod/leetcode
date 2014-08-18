class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = []
        if not path: return '/'
        i = 0
        while i < len(path):
            end = i + 1
            while end < len(path) and path[end] != '/':
                end += 1
            sub = path[i+1:end]
            if sub:
                if sub == '..':
                    if stack: stack.pop()
                elif sub != '.':
                    stack.append(sub)
            i = end
        result = ''
        if not stack: return '/'
        for i in stack:
            result = result + '/' + i
        return result
