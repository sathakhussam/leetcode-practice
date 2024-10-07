# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        c = 0
        temp = head
        while temp:
            c += 1
            temp = temp.next
        index = (c - n - 1) if c != n else 0


        if c == n and index == 0:
            return head.next
        
        c = 0
        temp = head
        prev = None
        while temp:
            prev = temp
            if c == index:
                try:
                    prev.next = temp.next.next
                except:
                    prev.next = None
                temp = temp.next
            else:
                temp = temp.next
            c += 1
        temp = head
        while temp:
            print(temp.val)
            temp = temp.next
        return head

s = Solution()
ll = ListNode(1)
ll.next = ListNode(2)
# ll.next.next = ListNode(3)
# ll.next.next.next = ListNode(4)
# ll.next.next.next.next = ListNode(5)
s.removeNthFromEnd(ll, 2)