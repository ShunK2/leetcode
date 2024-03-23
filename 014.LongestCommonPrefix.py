# leetcode 15. Longest Common Prefix という問題があります。この問題は、文字列の配列が与えられたとき、すべての文字列に共通する最長の接頭辞を見つけるというものです。この問題を解いてみましょう。
# 例えば、["flower", "flow", "flight"] という文字列の配列が与えられた場合、この配列の中で共通する最長の接頭辞は "fl" です。
# この問題を解くためのアルゴリズムは以下のようになります。
# 1. 文字列の配列が空の場合、空文字列を返します。
# 2. 文字列の配列の中で最小の文字列と最大の文字列を見つけます。
# 3. 最小の文字列と最大の文字列の共通する接頭辞を見つけます。
# 4. この接頭辞を返します。
# このアルゴリズムを実装したコードを以下に示します。
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        min_s = min(strs)
        max_s = max(strs)
        for i, c in enumerate(min_s):
            if c != max_s[i]:
                return min_s[:i]
        return min_s

solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"])) # "fl"
print(solution.longestCommonPrefix(["dog", "racecar", "car"])) # ""
print(solution.longestCommonPrefix(["ab", "a"])) # "a"