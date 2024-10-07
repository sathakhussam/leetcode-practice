# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        tmp = l1
        s1 = ""
        while tmp:
            s1 = str(tmp.val) + s1
            tmp = tmp.next
        tmp = l2
        s2 = ""
        while tmp:
            s2 = str(tmp.val) + s2
            tmp = tmp.next
        s1, s2 = int(s1), int(s2)
        head = None
        tmp = None
        for num in str(s1+s2)[::-1]:
            node = ListNode(int(num))
            if not head:
                head = node
            if not tmp:
                tmp = node
            else:
                tmp.next = node
                tmp = tmp.next
        return head

s = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

s.addTwoNumbers(l1,l2)