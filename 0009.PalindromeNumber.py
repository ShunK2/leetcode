# leetcode 9. Palindrome Number という問題があります。この問題は、整数が回文数であるかどうかを判定するというものです。この問題を解いてみましょう。
# 例えば、121 という整数が与えられた場合、121 は回文数なので True を返すようなアルゴリズムを設計してください。
# また、この問題には以下のような条件があります。
# 1. 整数を文字列に変換せずに回文数かどうかを判定してください。
# 2. 負の整数は回文数ではありません。
# この問題を解くためのアルゴリズムを設計し、実装してください。
# 例1：
# Input: x = 121
# Output: True
# 例2：
# Input: x = -121
# Output: False
# 例3：
# Input: x = 10
# Output: False
# 例4：
# Input: x = -101
# Output: False
# 例5：
# Input: x = 0
# Output: True
# 例6：
# Input: x = 123454321
# Output: True
class Solution:
     def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        copy, reverse = x, 0
        
        while copy:
            reverse = reverse * 10 + copy % 10
            copy //= 10
        
        return x == reverse

solution = Solution()
print(solution.isPalindrome(121)) # True
print(solution.isPalindrome(-121)) # False
print(solution.isPalindrome(10)) # False
print(solution.isPalindrome(-101)) # False
print(solution.isPalindrome(0)) # True
print(solution.isPalindrome(123454321)) # True