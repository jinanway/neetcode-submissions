# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        multiplier = 1
        while(l1 != None):
            num += (l1.val * multiplier)
            multiplier *= 10
            l1 = l1.next

        multiplier = 1
        while(l2 != None):
            num += (l2.val * multiplier)
            multiplier *= 10
            l2 = l2.next
        
        if(num == 0):
            return ListNode()

        head = ListNode()
        curr = head

        while(num):
            curr.next = ListNode(num % 10)
            curr = curr.next
            num = num // 10
        

        return head.next
