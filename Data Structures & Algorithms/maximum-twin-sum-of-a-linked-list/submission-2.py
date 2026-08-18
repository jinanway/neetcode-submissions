# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        first, second = head, head
        prev = None
        while(second and second.next):
            second = second.next.next
            temp = first.next
            first.next = prev
            prev = first
            first = temp
        best = 0
        while(first):
            if(first.val + prev.val > best):
                best = first.val + prev.val
            first = first.next
            prev = prev.next
        
        return best