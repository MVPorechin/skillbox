class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {"}": "{", ")": "(", "]": "["}
        stack = []

        for char in s:
            if char not in parentheses:
                stack.append(char)
            elif not stack or stack.pop() != parentheses[char]:
                return False
        return not stack


s = Solution()
print(s.isValid(s="(]"))