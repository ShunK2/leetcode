# 文字列であるsが与えられるのでその文字列の中で最も長い回文（どちらから読んでも同じになる）を探し出すようなアルゴリズムを設計してください。
# 例えば、文字列 "babad" が与えられた場合、"bab" または "aba" が答えとなります。
# また、文字列 "cbbd" が与えられた場合、"bb" が答えとなります。
# なお、この問題にはいくつかの解法が存在しますが、ここでは Manacher's Algorithm と呼ばれるアルゴリズムを使用して解いてみましょう。
# このアルゴリズムは、O(n) で最長の回文を求めることができます。
# 以下に Manacher's Algorithm の概要を示します。
# 1. 文字列 s の各文字の間や先頭、末尾に "#" を挿入して新しい文字列 s_new を作成します。
# 2. 配列 p を用意し、各要素を 0 で初期化します。
# 3. 変数 c と r を用意し、それぞれ 0 で初期化します。
# 4. 文字列 s_new の各文字について以下の処理を行います。
#     1. もし i が r より小さい場合、p[i] に min(r - i, p[2 * c - i]) を代入します。
#     2. s_new[i - p[i] - 1] と s_new[i + p[i] + 1] が同じ文字である限り、p[i] を 1 増やします。
#     3. もし i + p[i] が r より大きい場合、c と r を i と i + p[i] に更新します。
# 5. p の最大値を求め、その最大値を持つインデックスを max_index とします。
# 6. s の max_index から max_len だけ左に移動した文字列が最長の回文となります。
# 7. この回文を返します。
# このアルゴリズムを用いて、以下の関数を実装してください。
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_new = "#" + "#".join(s) + "#"
        print(s_new)
        n = len(s_new)
        p = [0] * n
        c = r = 0
        for i in range(n):
            if i < r:
                p[i] = min(r - i, p[2 * c - i])
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and s_new[i - p[i] - 1] == s_new[i + p[i] + 1]:
                p[i] += 1
                if i + p[i] > r:
                    c, r = i, i + p[i]
        max_len = max(p)
        max_index = p.index(max_len)
        return s[(max_index - max_len) // 2: (max_index + max_len) // 2]

solution = Solution()
print(solution.longestPalindrome("babad")) # "bab" or "aba"
print(solution.longestPalindrome("cbbd")) # "bb"
print(solution.longestPalindrome("a")) # "a"
print(solution.longestPalindrome("ac")) # "a"