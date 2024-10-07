# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left: int, right: int):

        if left == right:
            return head

        if left == 1:    
            c = 1
            pr = None
            ll = head
            nextt= ll.next
            
            while ll and c <= right:
                ll.next = pr
                pr = ll
                ll = nextt
                if ll:
                    nextt = ll.next
                c+= 1
            tt = pr
            while tt.next:
                tt = tt.next
            tt.next = ll
            head = pr
            return head
        ll = head
        pr = None
        nextt = ll.next
        c = 1

        while c < left:
            pr = ll
            ll = ll.next
            if ll:
                nextt = ll.next
            c += 1

        iHead = pr

        pr = None
        ll = ll
        nextt= ll.next
        
        while ll and c <= right:
            ll.next = pr
            pr = ll
            ll = nextt
            if ll:
                nextt = ll.next
            c+= 1
        
        if ll:
            tt = pr
            while tt.next:
                tt = tt.next
            tt.next = ll
        # pr.next = ll
        tt = head
        c = 1
        while tt.next and c +1 < left:
            tt = tt.next
            c+= 1
        tt.next = pr
        return head
            

s = Solution()

ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)

s.reverseBetween(ll, 1, 4)