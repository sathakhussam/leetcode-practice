"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        od = []
        odc = []
        tp = head
        while tp:
            od.append(tp)
            odc.append(Node(tp.val))
            tp = tp.next
        
        r = []
        for node in od:
            r.append(node.random)
        rIndex = []
        for rNode in r:
            if rNode == None:
                rIndex.append(None)
            else:
                for i in range(len(od)):
                    if rNode == od[i]:
                        rIndex.append(i)      
        # print(od, rIndex)
        head = None
        prev = None
        for i in range(len(rIndex)):
                
            odc[i].next = odc[i+1] if i+1 < len(rIndex) else None
            odc[i].random = odc[rIndex[i]] if rIndex[i] != None else None
            if prev:
                prev.next = odc[i]
            prev = odc[i]
            if head == None:
                head = odc[i]
        
        tp = head
        while tp:
            print(tp.val, tp.next.val if tp.next else None, tp.random.val if tp.random else None)
            tp = tp.next

        return head

# class Solution:
#     def copyRandomList(self, head):
#         if not head:
#             return None
        
#         # Step 1: Create a mapping from original nodes to their copies
#         old_to_new = {}
#         tp = head
#         while tp:
#             old_to_new[tp] = Node(tp.val)  # Create a new node for each original node
#             tp = tp.next
        
#         # Step 2: Assign next and random pointers for the new nodes
#         tp = head
#         while tp:
#             new_node = old_to_new[tp]
#             new_node.next = old_to_new.get(tp.next)  # Get the next node's copy
#             new_node.random = old_to_new.get(tp.random)  # Get the random node's copy
#             tp = tp.next
        
#         # Return the head of the new list
#         return old_to_new[head]

s = Solution()
# Creating the nodes
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

# Linking the next pointers
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Linking the random pointers
node1.random = None        # Node 7's random points to None
node2.random = node1       # Node 13's random points to Node 7
node3.random = node5       # Node 11's random points to Node 1
node4.random = node3       # Node 10's random points to Node 11
node5.random = node1       # Node 1's random points to Node 7

s.copyRandomList(node1)