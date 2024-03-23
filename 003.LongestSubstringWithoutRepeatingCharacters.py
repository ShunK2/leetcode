# 問題としては、文字列が与えられたとき、文字を繰り返さずに最長の部分文字列の長さを求めなさいというものです。
# 例えば、"abcabcbb"の場合、最長の部分文字列は"abc"であり、その長さは3です。
# この問題は、スライディングウィンドウというアルゴリズムを用いて解くことができます。
# 具体的には、以下のようなアルゴリズムで実装することができます。
# 1. 文字列の先頭から順に文字を取り出していきます。
# 2. その文字がすでに登場している場合、その文字が登場するまでの部分文字列を削除します。
# 3. 文字が登場していない場合、その文字を部分文字列に追加します。
# 4. このとき、最長の部分文字列の長さを更新します。
# 5. 与えられた文字列の最後までこの処理を行い、最終的な最長の部分文字列の長さを返します。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[c] = i
        return max_length
    
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb")) # 3
print(solution.lengthOfLongestSubstring("bbbbb")) # 1
print(solution.lengthOfLongestSubstring("pwwkew")) # 3
print(solution.lengthOfLongestSubstring("")) # 0