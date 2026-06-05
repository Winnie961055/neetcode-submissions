# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Tortoise and Hare

        fast = head
        slow = head

        while fast and fast.next: # fast 要一次走兩步，所以要確保 fast 和 fast.next 都存在

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

