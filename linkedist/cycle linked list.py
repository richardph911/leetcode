# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# fast move 2 step and slow 1 step, if they meet again then has cycle
# check if cycle
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast!= None and fast.next != None :
            fast = fast.next.next
            slow = slow.next
            if(fast == slow):
                return True
        return False
