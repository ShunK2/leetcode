# leetcode 11. Container With Most Water という問題があります。この問題は、整数の配列が与えられたとき、配列の要素が x 軸に、配列の値が y 軸に対忘して表されるグラフの中で、最も多くの水を含む容器を見つけるというものです。この問題を解いてみましょう。
# 例えば、[1, 8, 6, 2, 5, 4, 8, 3, 7] という配列が与えられた場合、この配列が表すグラフは以下のようになります。
# 8 |       ■                   ■
# 7 |       ■                   ■       ■
# 6 |       ■   ■               ■       ■
# 5 |       ■   ■       ■       ■       ■
# 4 |       ■   ■       ■   ■   ■       ■
# 3 |       ■   ■       ■   ■   ■   ■   ■
# 2 |       ■   ■   ■   ■   ■   ■   ■   ■
# 1 |   ■   ■   ■   ■   ■   ■   ■   ■   ■
#    -------------------------------------
#       0   1   2   3   4   5   6   7   8
# この場合、(1, 8) という組み合わせが最も多くの水を含む容器となります。そのため、この場合の出力は 49 となります。
# この問題を解くためのアルゴリズムは以下のようになります。
# 1. 配列の先頭と末尾のインデックスをそれぞれ left と right として定義します。
# 2. left と right の差を width として定義します。
# 3. left と right の値を比較し、小さい方を height として定義します。
# 4. width と height の積を計算し、これを area として定義します。
# 5. area が最大値であれば、これを max_area として定義します。
# 6. height が小さい方のインデックスを 1 つ進めます。
# 7. 2 に戻り、left と right の値を更新して計算を続けます。
# 8. left と right が交差するまで 2 から 7 を繰り返します。
# 9. max_area を返します。
# この問題を解くためのアルゴリズムを設計し、実装してください。
# 例1：
# Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
# 例2：
# Input: height = [1, 1]
# Output: 1
# 例3：
# Input: height = [4, 3, 2, 1, 4]
# Output: 16
class Solution:
    def maxArea(self, height) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            area = width * h
            max_area = max(max_area, area)
        return max_area

solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])) # 49
print(solution.maxArea([1, 1])) # 1
print(solution.maxArea([4, 7, 3, 1, 7])) # 16