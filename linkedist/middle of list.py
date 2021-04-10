# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#*********************************'
# ' using fast and slow method
#*********************************'

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp = head
        while temp and temp.next:
            temp = temp.next.next
            head = head.next
        return head
            
        # fast = head
        # slow = head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        # return slow
