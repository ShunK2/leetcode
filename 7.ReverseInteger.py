# 32ビット符号付き整数xが与えられたとき、整数の逆数を計算するアルゴリズムを設計してください
# 結果が32ビット整数の範囲に収まらない場合は、0を返します
# 例1：
# Input: x = 123
# Output: 321
# 例2：
# Input: x = -123
# Output: -321
# 例3：
# Input: x = 120
# Output: 21
# 例4：
# Input: x = 0
# Output: 0
# 例5：
# Input: x = 1534236469
# Output: 0
# 例6：
# Input: x = -2147483648
# Output: 0
# 制約：
# -231 <= x <= 231 - 1
# ==============================================================================
# 32ビット符号付き整数の範囲は-2,147,483,648から2,147,483,647までです
class Solution:
    def reverse(self, x: int) -> int:
        max_32 = 2**31 - 1
        if abs(x) > max_32:
            return 0

        if x < 0:
            reverse_int = -1
            x = x * reverse_int
        else:
            reverse_int = 1
        revN = 0
        while x > 0:
            revN = revN * 10 + x % 10
            x //= 10

        if abs(revN) > max_32:
            return 0
        else:
            return reverse_int * revN

solution = Solution()
print(solution.reverse(123)) # 321
print(solution.reverse(-123)) # -321
print(solution.reverse(120)) # 21
print(solution.reverse(0)) # 0
print(solution.reverse(1534236469)) # 0