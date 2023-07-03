class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_index = 0
        right_index = len(s) - 1

        while left_index < right_index:
            while not (s[left_index].isdigit() or s[left_index].isalpha()) and left_index < right_index:
                left_index += 1
            while not (s[right_index].isdigit() or s[right_index].isalpha()) and left_index < right_index:
                right_index -= 1
            if s[left_index] != s[right_index]:
                if (s[left_index + 1] == s[right_index - 1]) or (s[left_index + 1] == s[right_index]) or s[left_index] == s[right_index - 1]:
                    return True
                else:
                    return False
            left_index += 1
            right_index -= 1
        return True


my_sol = Solution()
print(my_sol.validPalindrome(s='EECCCCBEBAEEABEBCCCEEA'))