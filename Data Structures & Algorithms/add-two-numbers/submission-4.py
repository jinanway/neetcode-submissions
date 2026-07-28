# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        curr = head
        
        hold = 0
        while(l1 != None and l2 != None):
            num = l1.val + l2.val + hold
            hold = 0
            if(num >= 10):
                curr.next = ListNode(num % 10)
                hold = num // 10
            else:
                curr.next = ListNode(num)
            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        if(l1 != None):
            while(l1 != None):
                num = l1.val + hold
                hold = 0
                if(num >= 10):
                    curr.next = ListNode(num % 10)
                    hold = num // 10
                else:
                    curr.next = ListNode(num)
                l1 = l1.next
                curr = curr.next
        if(l2 != None):
            while(l2 != None):
                num = l2.val + hold
                hold = 0
                if(num >= 10):
                    curr.next = ListNode(num % 10)
                    hold = num // 10
                else:
                    curr.next = ListNode(num)
                l2 = l2.next
                curr = curr.next
        if(hold != 0):
            curr.next = ListNode(hold)
            curr = curr.next
        return head.next