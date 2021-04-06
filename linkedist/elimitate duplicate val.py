#Input: head = [1,2,6,3,4,5,6], val = 6
#Output: [1,2,3,4,5]
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode() # create dummy nothing node
        dummy.next = head # and point to head in case the val is at beginning
        current = dummy
        while current.next: #if still not end
            if current.next.val==val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
