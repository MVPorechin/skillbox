class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_value = arr[-1]
        for index in range(len(arr), 0, -1):

            if arr[index-1] > max_value:
                max_value = arr[index - 1]
            elif arr[index-1] < max_value:
                arr[index-1] = max_value

        arr.remove(arr[0])
        arr.append(-1)
        return arr


my_sol = Solution()
rt=my_sol.replaceElements(arr=[17,18,5,4,6,1])

print(rt)