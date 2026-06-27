'''
find the middle

reverse the second half

merge the two lists


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #the head of the second half is slow.next
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse the second half
        second = slow.next
        prev = None
        slow.next = prev

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp


        #merge the two lists
        first, second  = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        
        

        
        

        
        