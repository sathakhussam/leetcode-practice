# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        c = 0
        temp = head
        while temp:
            c+=1
            temp = temp.next
        if c == 0:
            return head
        k = k % c 
        if k == 0:
            return head

        # Getting Index Element
        lastIndex = c - k - 1
        lastElement = head
        i = 0
        while lastElement and i < lastIndex:
            lastElement = lastElement.next
            i+=1
        
        lastLast = lastElement
        while lastLast.next:
            lastLast = lastLast.next

        head, lastElement.next, lastLast.next = lastElement.next, None, head
        temp = head
        return head
        while temp:
            print(temp.val)
            temp = temp.next






s = Solution()
ll = ListNode(1)
# ll.next = ListNode(2)
# ll.next.next = ListNode(3)
# ll.next.next.next = ListNode(4)
# ll.next.next.next.next = ListNode(5)

s.rotateRight(ll, 1)