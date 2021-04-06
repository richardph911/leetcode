# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# lan 2: thi current = 2
# then current.next point to pre la 1: 1 <--2: point back ward

#Input: head = [1,2,3,4,5]
#Output: [5,4,3,2,1]
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = None
        next = head
        while next:
            current = next # current = 1 then 2 then 3 then 4..
            next = current.next # next = 2 , then 3, then 4..
            current.next = prev # point to prev:  1 -> None, 1 <--- 2
            prev = current # pre = 1 -> None, tao thanh. linklist nhu current
        return prev
