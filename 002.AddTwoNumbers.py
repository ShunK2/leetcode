# 空ではない連結リストを与えられるので与えられた数字をそれぞれ桁ごとに足していき、反転させて返すようなアルゴリズムを設計してください、というものです。
# 例えば、(2 -> 4 -> 3) + (5 -> 6 -> 4) = 7 -> 0 -> 8 となります。
# この問題は、リストの先頭から順に足し算を行い、桁上がりを考慮する必要があります。具体的には、以下のようなアルゴリズムで実装することができます。
# 1. 与えられたリストの先頭から順に、桁上がりを考慮して足し算を行います。
# 2. 足し算の結果が10以上の場合、次の桁に1を加算します。
# 3. 与えられたリストの最後まで足し算を行い、最終的な結果を返します。
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def __str__(self):
        return f"ListNode{{val: {self.val}, next: {self.next}}}"

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tempsum = 0
        root = ListNode(0)
        cur = root
        while l1 or l2 or tempsum:
            if l1: tempsum += l1.val; l1 = l1.next
            if l2: tempsum += l2.val; l2 = l2.next

            cur.next = ListNode(tempsum % 10)
            cur = cur.next
            tempsum //= 10
        return root.next

solution = Solution()

l1 = ListNode(2,ListNode(4,ListNode(3))) #(2 -> 4 -> 3)
l2 = ListNode(5,ListNode(6,ListNode(4))) #(5 -> 6 -> 4)

print(solution.addTwoNumbers(l1, l2)) # 7 -> 0 -> 8
