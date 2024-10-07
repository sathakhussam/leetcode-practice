# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1 and list2:
            return list2
        if not list2 and list1:
            return list1
        if not list2 and not list1:
            return None
        
        t1 = list1
        t2 = list2
        head = None
        n = None
        while t1 or t2:
            c1 = 101 
            c2 = 101 
            if t1:
                c1 = t1.val
            if t2:
                c2 = t2.val
            if c1 < c2:
                node = ListNode(c1)
                if not head:
                    head = node
                    n = node
                else:
                    n.next = node
                    n = n.next

                if t1:
                    t1 = t1.next            
            elif c1 > c2:
                node = ListNode(c2)

                if not head:
                    head = node
                    n = node
                else:
                    n.next = node
                    n = n.next
                if t2:
                    t2 = t2.next
            elif c1 == c2:
                if c1 == c2 and c1 ==101:
                    break
                node = ListNode(c2)
                if c1 != 101:
                    node2 = ListNode(c1)
                    node.next = node2
                    
                if not head:
                    head = node
                    n = node
                else:
                    n.next = node
                    n = n.next
                if c1 != 101:
                    n = node.next
                if t1:
                    t1 = t1.next
                if t2:
                    t2 = t2.next
        tmp = head
        while tmp:
            print(tmp.val)
            tmp = tmp.next
        return head
            

s = Solution()

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

s.mergeTwoLists(l1,l2)