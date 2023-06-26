class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = []
        index = 0
        # pure_string = ''.join(sym for sym in s if sym.isalpha()).lower()
        # if len(pure_string) % 2 == 0:
        #     length = len(pure_string)
        # else:
        #     length = len(pure_string) - 1
        # if pure_string[:length] == pure_string[length:]:
        #     return True
        while index != len(s) // 2:

            if s[index].isalpha() == s[-index].isalpha() and s[index] == s[-index]:
                result.append(True)
            else:
                result.append(False)
            index += 1

        # if all(result):
        #     return True


my_solution = Solution()
print(my_solution.isPalindrome(s="A man, a plan, a canal: Panama"))
