# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x: int):
        aHead = None
        a = None
        bHead = None
        b = None
        tmp = head
        if not head:
            return None
        while tmp:
            if tmp.val >= x:
                if not b:
                    bHead = ListNode(tmp.val)
                    b = bHead
                else:
                    b.next = ListNode(tmp.val)
                    b = b.next
            else:
                if not a:
                    aHead = ListNode(tmp.val)
                    a = aHead
                else:
                    a.next = ListNode(tmp.val)
                    a = a.next
            tmp = tmp.next
        if a:
            a.next = bHead
        # tmp = head
        # while tmp:
        #     print(tmp.val)
        #     tmp = tmp.next
        return aHead if aHead else bHead 
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

s = Solution()
s.partition(head, 3)