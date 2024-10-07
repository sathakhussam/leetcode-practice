# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        temp = head
        arr = ""
        arr_t = ""
        f = False
        while temp:
            tval = "+" + str(temp.val) if temp.val >= 0 else str(temp.val) 
            print(str(tval))
            if len(arr_t) != 3:
                if arr_t + " " + str(tval) in arr:
                    if arr.count(arr_t) != 2:
                        f= True
                        break
                    arr_t = arr_t + " " + str(tval)
                else:
                    # f = True
                    break
                    arr_t = ""
            elif str(tval) in arr:
                arr_t = arr_t + " " + str(tval)
            
            arr = arr+ " " +str(tval)
            temp = temp.next
        return f


s = Solution()
ll = ListNode(-1)
ll.next = ListNode(-7)
ll.next.next = ListNode(7)
ll.next.next.next = ListNode(-4)
ll.next.next.next.next = ListNode(19)
ll.next.next.next.next.next = ListNode(6)
ll.next.next.next.next.next.next = ListNode(-9)
ll.next.next.next.next.next.next.next = ListNode(-5)
ll.next.next.next.next.next.next.next.next = ListNode(-2)
ll.next.next.next.next.next.next.next.next.next = ListNode(-5)
ll.next.next.next.next.next.next.next.next.next.next = ll.next.next
ll.next.next.next.next.next.next.next.next.next.next = ll.next.next.next.next.next


s.hasCycle(ll)