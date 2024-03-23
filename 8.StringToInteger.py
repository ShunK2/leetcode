# leetcode 8. String to Integer (atoi) という問題があります。この問題は、文字列を整数に変換するというものです。この問題を解いてみましょう。
# 例えば、"42" という文字列が与えられた場合、整数 42 を返すようなアルゴリズムを設計してください。
# また、この問題には以下のような条件があります。
# 1. 文字列の前後には空白が含まれている可能性があります。
# 2. 文字列の先頭には正負の符号が含まれている可能性があります。
# 3. 文字列の中には数字以外の文字が含まれている可能性があります。
# 4. 文字列の先頭から数字以外の文字が出現した場合、それ以降の文字列は無視してください。
# 5. 整数は 32 ビットの範囲で表現する必要があります。つまり、-2^31 <= x <= 2^31 - 1 の範囲である必要があります。
# 6. 整数として表現できない場合は、0 を返してください。
# この問題を解くためのアルゴリズムを設計し、実装してください。
# 例1：
# Input: str = "42"
# Output: 42
# 例2：
# Input: str = "   -42"
# Output: -42
# 例3：
# Input: str = "4193 with words"
# Output: 4193
# 例4：
# Input: str = "words and 987"
# Output: 0
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        if s[0] in ['+', '-']:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        else:
            sign = 1
        num = 0
        for c in s:
            if not c.isdigit():
                break
            num = num * 10 + int(c)
        num *= sign
        if num > 2**31 - 1:
            return 2**31 - 1
        elif num < -2**31:
            return -2**31
        else:
            return num

solution = Solution()
print(solution.myAtoi("42")) # 42
print(solution.myAtoi("   -42")) # -42
print(solution.myAtoi("4193 with words")) # 4193
print(solution.myAtoi("words and 987")) # 0
print(solution.myAtoi("-91283472332")) # -2147483648
print(solution.myAtoi("3.14159")) # 3