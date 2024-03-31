# leetcode 12. Integer to Roman という問題があります。この問題は、整数をローマ数字に変換するというものです。この問題を解いてみましょう。
# 例えば、3 という整数が与えられた場合、3 はローマ数字の III に変換されます。そのため、この場合の出力は "III" となります。
# また、この問題には以下のような条件があります。
# 1. 1 <= num <= 3999 の範囲の整数が与えられます。
# 2. ローマ数字は以下の文字を使って表現されます。
#     - I: 1
#     - V: 5
#     - X: 10
#     - L: 50
#     - C: 100
#     - D: 500
#     - M: 1000
# 3. ローマ数字は次のような規則で表現されます。
#     - 1 から 3 までの整数は I が連続して使われます。
#     - 4 は IV で表現されます。
#     - 5 から 8 までの整数は V に続けて I が使われます。
#     - 9 は IX で表現されます。
#     - 10 から 30 までの整数は X が連続して使われます。
#     - 40 は XL で表現されます。
#     - 50 から 80 までの整数は L に続けて X が使われます。
#     - 90 は XC で表現されます。
#     - 100 から 300 までの整数は C が連続して使われます。
#     - 400 は CD で表現されます。
#     - 500 から 800 までの整数は D に続けて C が使われます。
#     - 900 は CM で表現されます。
#     - 1000 から 3000 までの整数は M が連続して使われます。
# この問題を解くためのアルゴリズムを設計し、実装してください。
# 例1：
# Input: num = 3
# Output: "III"
# 例2：
# Input: num = 4
# Output: "IV"
# 例3：
# Input: num = 9
# Output: "IX"
# 例4：
# Input: num = 58
# Output: "LVIII"
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        for i, r in [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]:
            while num >= i:
                roman += r
                num -= i
        return roman
    
solution = Solution()
print(solution.intToRoman(3)) # "III"
print(solution.intToRoman(4)) # "IV"
print(solution.intToRoman(9)) # "IX"
print(solution.intToRoman(58)) # "LVIII"