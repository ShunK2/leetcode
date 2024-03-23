# leetcode 21. Merge Two Sorted Lists という問題があります。この問題は、2 つのソートされたリストが与えられたとき、これらのリストをマージして新しいソートされたリストを返すというものです。この問題を解いてみましょう。
# 例えば、以下の 2 つのリストが与えられた場合、
# l1 = [1, 2, 4]
# l2 = [1, 3, 4]
# 以下のようなリストを返します。
# [1, 1, 2, 3, 4, 4]
# この問題を解くためのアルゴリズムは以下のようになります。
# 1. 2 つのリストをマージしてソートします。
# 2. マージしたリストを返します。
# このアルゴリズムを実装したコードを以下に示します。
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def __str__(self):
        return f"ListNode{{val: {self.val}, next: {self.next}}}"

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode()
        cur = root
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return root.next

solution = Solution()
l1 = ListNode(1,ListNode(2,ListNode(4))) # [1, 2, 4]
l2 = ListNode(1,ListNode(3,ListNode(4))) # [1, 3, 4]
print(solution.mergeTwoLists(l1, l2)) # [1, 1, 2, 3, 4, 4]