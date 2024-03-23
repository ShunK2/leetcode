# leetcode 13. Roman to Integer という問題があります。この問題は、ローマ数字が与えられたとき、これを整数に変換するというものです。この問題を解いてみましょう。
# 例えば、"III" というローマ数字が与えられた場合、これは整数 3 に変換されます。そのため、この場合の出力は 3 となります。
# また、この問題には以下のような条件があります。
# 1. ローマ数字は以下の文字を使って表現されます。
#     - I: 1
#     - V: 5
#     - X: 10
#     - L: 50
#     - C: 100
#     - D: 500
#     - M: 1000
# 2. ローマ数字は次のような規則で表現されます。
#     - 1 から 3 までの整数は I が連続して使われます。
#     - 4 は IV で表現されます。
#     - 5 から 8 までの整数は V に続けて I が使われます。

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        prev = 0
        for c in s:
            curr = roman[c]
            num += curr
            if curr > prev:
                num -= 2 * prev
            prev = curr
        return num
    
solution = Solution()
print(solution.romanToInt("III")) # 3
print(solution.romanToInt("IV")) # 4
print(solution.romanToInt("IX")) # 9