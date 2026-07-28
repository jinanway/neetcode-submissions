# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        while(l1 != None):
            num1 = str(l1.val) + num1
            l1 = l1.next
        
        num2 = ""
        while(l2 != None):
            num2 = str(l2.val) + num2
            l2 = l2.next
        
        num1 = int(num1)
        num2 = int(num2)
        num = num1 + num2
            
        
        head = ListNode()
        curr = head

        if(num == 0):
            head.next = ListNode(0)

        while(num != 0):
            curr.next = ListNode(num % 10)
            num = num // 10
            curr = curr.next
        
        return head.next
