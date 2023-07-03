class Solution(object):
    def is_palindrome(self, s):
        left_index = 0
        right_index = len(s) - 1
        while left_index < right_index:
            if s[left_index] == s[right_index]:
                left_index += 1
                right_index -= 1
            else:
                return False
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_index = 0
        right_index = len(s) - 1
        while left_index < right_index:
            if s[left_index] == s[right_index]:
                left_index += 1
                right_index -= 1
            else:
                return self.is_palindrome(s[left_index + 1:right_index+1]) or self.is_palindrome(s[left_index:right_index])
        return True


my_sol = Solution()
print(my_sol.validPalindrome(s='EECCCCBEBAEEABEBCCCEEA'))