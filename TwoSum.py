# 問題としては、整数の入った配列と特定の値が格納された変数targetが与えられます。配列の中から二つの整数を選び、targetと一致する組み合わせを見つけ、配列のインデックスを返すような関数を実装してください。
# なお、その組み合わせは一つしか存在せず、かつ同じ値を二度使うことは許されません。

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