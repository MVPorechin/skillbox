class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        left, right = len(arr) - 2, len(arr) - 1
        max_value = 0
        while left > 0:
            for index in range(len(arr), 0, -1):
                if len(arr) == 1:
                    arr[-1] = -1
                elif arr[index - 1] > max_value:
                    max_value = arr[index - 1]
                elif arr[index - 1] < max_value:
                    arr[index - 1] = max_value
                elif arr[right] <= arr[left]:
                    arr[left] = arr[right]
                    right -= 1

                left -= 1
        arr.remove(arr[0])
        arr.append(-1)
        return arr


my_sol = Solution()
my_sol.replaceElements(arr=[17,18,5,4,6,1])

print(my_sol)