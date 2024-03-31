# leetcode 20. Valid Parentheses という問題があります。この問題は、文字列が与えられたとき、その文字列の中の括弧が正しく閉じられているかどうかを判定するというものです。この問題を解いてみましょう。
# 例えば、"()" や "()[]{}" は正しく閉じられているので True を返します。一方、"(]" や "([)]" は正しく閉じられていないので False を返します。
# この問題を解くためのアルゴリズムは以下のようになります。
# 1. 文字列の中の括弧をスタックに格納します。
# 2. 開き括弧が出現した場合、スタックに格納します。
# 3. 閉じ括弧が出現した場合、スタックから開き括弧を取り出します。
# 4. このとき、スタックが空であれば True を返します。
# 5. このアルゴリズムを実装したコードを以下に示します。
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return not stack

solution = Solution()
print(solution.isValid("()")) # True
print(solution.isValid("()[]{}")) # True
print(solution.isValid("(]")) # False