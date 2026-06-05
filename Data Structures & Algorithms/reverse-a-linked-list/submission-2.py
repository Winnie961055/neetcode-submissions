# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Recursion - Time: O(n) Space: O(n)
        
        def reverse(curr, prev):

            if curr is None:
                return prev
            
            else:
                next = curr.next
                curr.next = prev
                
                return reverse(next, curr)

        return reverse(head, None)    


        