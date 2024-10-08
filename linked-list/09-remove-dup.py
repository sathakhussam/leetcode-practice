# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        dc = {}
        tmp = head
        while tmp:
            if tmp.val in dc:
                dc[tmp.val] += 1
            else:
                dc[tmp.val] = 1
            tmp = tmp.next
        print(dc)

        tmp = head
        prev = None
        while tmp:
            if dc[tmp.val] > 1:
                if not prev:
                    head = tmp.next
                else:
                    prev.next = tmp.next
                tmp = tmp.next
            else:
                prev = tmp
                tmp = tmp.next

        return head
        # tmp = head
        # while tmp:
        #     print(tmp.val)
        #     tmp = tmp.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)

s = Solution()
s.deleteDuplicates(head)