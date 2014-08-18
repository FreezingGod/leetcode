# this is a bit cheating using python
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        lst = path.split('/')
        stack = []
        for i in lst:
            if not i or i == '.':
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return '/' + '/'.join(stack)
