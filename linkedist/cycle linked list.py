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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # since only tail has cycle.
        headSet = set()
        while head is not None:
            if head in headSet:
                return True
            headSet.add(head)
            head = head.next
        return False
    # time 0(n) : visit each of the n elements at most once. Adding a node to the hash takes 0(1) time
    # space 0(n): the space depends on the number of elements added to the has table
