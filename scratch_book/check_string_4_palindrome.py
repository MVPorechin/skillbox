import re


class Solution(object):
    def isPalindrome(self, s):
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
            if s[left_index].lower() != s[right_index].lower():
                return False
            left_index += 1
            right_index -= 1
        return True

        # Понравилось решение, я изначально подобно размышлял, то предлагал сравнивать срез на пополам.
        # А тут более элегантное.

        pure_string = re.sub(r'[\W_]', '', s)
        pure_string = pure_string.lower()

        if pure_string == pure_string[::-1]:
            return True

        return False


my_solution = Solution()
print(my_solution.isPalindrome(s="A man, a plan, a canal: Panama"))
