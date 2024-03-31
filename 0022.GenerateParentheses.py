# leetcode 22. Generate Parentheses という問題があります。この問題は、整数 n が与えられたとき、n 対の括弧で可能なすべての組み合わせを返すというものです。この問題を解いてみましょう。
# 例えば、n = 3 の場合、以下の組み合わせが可能です。
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
class Solution:
    def generateParenthesis(self, n: int):
        def backtrack(s = '', left = 0, right = 0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        res = []
        backtrack()
        return res

solution = Solution()
print(solution.generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
print(solution.generateParenthesis(1)) # ["()"]
print(solution.generateParenthesis(2)) # ["(())","()()"]