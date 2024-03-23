# leetcode 15. 3Sum という問題があります。この問題は、整数の配列が与えられたとき、その配列の中から 3 つの整数を選んで足し合わせた結果が 0 になる組み合わせをすべて見つけるというものです。この問題を解いてみましょう。
# 例えば、配列 [-1, 0, 1, 2, -1, -4] が与えられた場合、以下の組み合わせが 0 になります。
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
# この場合、答えは 2 つの組み合わせです。
# この問題を解くためのアルゴリズムは以下のようになります。
# 1. 配列をソートします。
# 2. 3 つの整数を選ぶために 3 つのループを回します。
# 3. 3 つの整数の合計が 0 になる組み合わせを見つけます。
# 4. このとき、組み合わせを返します。
# このアルゴリズムを実装したコードを以下に示します。
class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4])) # [[-1, -1, 2], [-1, 0, 1]]
print(solution.threeSum([])) # []
print(solution.threeSum([0])) # []
print(solution.threeSum([0, 0, 0])) # [[0, 0, 0]]