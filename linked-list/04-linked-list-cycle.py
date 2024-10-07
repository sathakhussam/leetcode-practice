# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        i = head
        if not head or not head.next or not head.next.next:
            return False
        j = head.next.next
        while i != j:
            if not i or not j or not i.next or not j.next or not j.next.next:
                return False
            i = i.next
            j = j.next.next
        if i == j:
            return True
        return False
            
