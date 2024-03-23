# leetcode 10. Regular Expression Matching という問題があります。この問題は、文字列とパターンが与えられたとき、パターンが文字列と一致するかどうかを判定するというものです。この問題を解いてみましょう。
# 例えば、文字列 "aa" とパターン "a" が与えられた場合、パターン "a" は文字列 "aa" と一致しないので False を返すようなアルゴリズムを設計してください。
# また、この問題には以下のような条件があります。
# 1. パターンには次の文字が含まれることがあります。
#     - '.' は任意の一文字に一致します。
#     - '*' は直前の文字が 0 回以上繰り返されることを表します。
# 2. パターンは空になることはありません。
# 3. 文字列は空になることがあります。
# この問題を解くためのアルゴリズムを設計し、実装してください。
# 例1：
# Input: s = "aa", p = "a"
# Output: False
# 例2：
# Input: s = "aa", p = "a*"
# Output: True
# 例3：
# Input: s = "ab", p = ".*"
# Output: True
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])

solution = Solution()
print(solution.isMatch("aa", "a")) # False
print(solution.isMatch("aa", "a*")) # True
print(solution.isMatch("ab", ".*")) # True
print(solution.isMatch("aab", "c*a*b")) # True
print(solution.isMatch("mississippi", "mis*is*p*.")) # False