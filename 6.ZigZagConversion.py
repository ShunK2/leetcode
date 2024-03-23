# このコードは、与えられた文字列を指定された行数でジグザグパターンに変換する機能を持っています。例えば、文字列 "PAYPALISHIRING" を3行で変換する場合、以下のようなパターンになります。
# P   A   H   N
# A P L S I I G
# Y   I   R
# この場合、変換された文字列は "PAHNAPLSIIGYIR" になります。
# この問題は、与えられた文字列を指定された行数でジグザグパターンに変換することで解くことができます。
# 具体的には、以下のようなアルゴリズムで実装することができます。
# 1. 行数が1の場合、文字列をそのまま返します。
# 2. 行数が文字列の長さ以上の場合、文字列をそのまま返します。
# 3. 行数が2以上の場合、行数分のリストを作成します。
# 4. 文字列を先頭から順に走査し、リストに文字を追加していきます。
# 5. 文字列の最後まで走査した後、リストを結合して返します。

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        index, step = 0, 1
        for char in s:
            rows[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(rows)
    
solution = Solution()
print(solution.convert("PAYPALISHIRING", 3)) # "PAHNAPLSIIGYIR"
print(solution.convert("PAYPALISHIRING", 4)) # "PINALSIGYAHRPI"

