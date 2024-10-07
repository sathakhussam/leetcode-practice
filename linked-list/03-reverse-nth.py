# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, head, k):
        c = 0
        if not head:
            return None
        prev = None
        ll = head
        after = ll.next

        tt = 1
        thead = head
        while thead:
            thead = thead.next
            tt+=1
        if tt <= k:
            return head
        
        while ll and c<k:
            ll.next = prev
            prev = ll
            ll = after
            if ll:
                after = ll.next
            c+=1
        if ll:
            tt = prev
            while tt.next:
                tt = tt.next
            tt.next = ll
        return prev
    def reverseKGroup(self, head, k: int):
        temp = head
        c = 0
        while temp:
            # print(c%k==0)
            if c%k == 0:
                c+=1
                if c - 1 == 0:
                    og = None
                else:
                    og = temp
                    temp = temp.next
                temp_head = self.reverse(temp, k)
                temp =  temp_head
                if c - 1 == 0:
                    head = temp
                tt = temp
                if c - 1 != 0 and og:
                    og.next = tt
                while tt and tt.next and c%k!=0:
                    print(tt.val)
                    tt = tt.next
                    c+=1
                temp = tt
            else:
                temp = temp.next
                c+=1
        # tt = head
        # while tt:
        #     print(tt.val)
        #     tt = tt.next
        return head
        

s = Solution()
ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)
s.reverseKGroup(ll, 3)