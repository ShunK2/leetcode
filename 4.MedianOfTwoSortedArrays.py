# 問題としては、サイズmとnの2つのソートされた配列nums1とnums2がある。2つの並べ替え配列の中央値を求めよ。
# この問題は、2つの配列をマージしてソートし、中央値を求めることで解くことができます。
# 具体的には、以下のようなアルゴリズムで実装することができます。
# 1. 2つの配列をマージしてソートします。
# 2. 配列の長さが奇数の場合、中央値はソートされた配列の長さを2で割った値になります。
# 3. 配列の長さが偶数の場合、中央値はソートされた配列の長さを2で割った値とその1つ前の値の平均になります。
# 4. このとき、中央値を返します。
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums)
        if n % 2 == 0:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2
        else:
            return nums[n // 2]

solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2])) # 2.0
print(solution.findMedianSortedArrays([1, 2], [3, 4])) # 2.5
print(solution.findMedianSortedArrays([0, 0], [0, 0])) # 0.0