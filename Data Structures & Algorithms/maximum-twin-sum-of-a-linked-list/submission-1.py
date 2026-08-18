# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next 

        l = 0
        r = len(nums) - 1
        best = 0
        while (l < r):
            if(nums[l] + nums[r] > best):
                best = nums[l] + nums[r]
            l += 1
            r -= 1
            
        return best