# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# lan 2: thi current = 2
# then current.next point to pre la 1: 1 <--2: point back ward
class Solution:
    
    # idea is to make 1 <--2 (pre <--current)
    # current, current.next, set previous value to current
    # then we need: prev, current node.
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = None
        while head:
            # at 2nd round
            current = head # current = 2
            head = current.next # head = 3
            current.next = previous # 2 point to 1
            previous = current # previous = 2
        return previous
            
        
    # def reverseList(self, head: ListNode) -> ListNode:
    #     prev = None
    #     current = None
    #     next = head
    #     while next:
    #         current = next # current = 1 then 2 then 3 then 4..
    #         next = current.next # next = 2 , then 3, then 4..
    #         current.next = prev # point to prev:  1 -> None, 1 <--- 2
    #         prev = current # pre = 1 -> None, tao thanh. linklist nhu current
    #     return prev
            
            
            
      
        
