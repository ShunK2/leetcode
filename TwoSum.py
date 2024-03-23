class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            y = target - num
            if y in d:
                return [d[y], i]
            d[num] = i
        return []

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9)) # [0, 1]