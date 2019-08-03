# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        curr_node = head

        if m == 1:
            prev_node = head
            curr_node = head.next
            first_reversed_node = head
        else:
            for _ in range(m - 2):
                curr_node = curr_node.next
            anchor_node = curr_node
            first_reversed_node = curr_node.next
            prev_node = curr_node.next
            curr_node = curr_node.next.next
        
        for _ in range(n - m):
            next_node = curr_node.next
            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = next_node
        
        first_reversed_node.next = curr_node

        if m == 1:
            return prev_node
        else:
            anchor_node.next = prev_node
            return head


first = ListNode(0)
prev = first
for i in range(1, 5):
    x = ListNode(i)
    prev.next = x
    prev = x

def printit(node):
    while node is not None:
        print(node.val)
        node = node.next
        
printit(first)
print("start-------")
z = Solution().reverseBetween(first, 1, 2)
print("SOLUTION++++")
printit(z)