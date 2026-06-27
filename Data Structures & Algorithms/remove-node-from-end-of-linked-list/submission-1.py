'''

use two pointer technique(create a dummy node in case we're going to remove the first node)
create a two pointer with a range of n
when the right pointer moves to the end, the left pointer will be one step before the node that should be removed
remove the node and return the head 
if we remove head and return head, then the old head will be removed
so should return dummy.next


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
 

        