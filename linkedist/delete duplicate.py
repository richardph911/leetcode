# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Input: head = [1,1,2]
#Output: [1,2]
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            if current.next.val==current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head # since current = head. now current is None so need head to return the list
 
            
            
            
