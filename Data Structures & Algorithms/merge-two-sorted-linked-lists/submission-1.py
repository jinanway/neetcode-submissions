class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 == None):
            return list2
        if(list2 == None):
            return list1
        
        merged = ListNode()
        curr = merged

        while(list1 != None and list2 != None):
            if(list1.val < list2.val):
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next
        
        if(list1 == None):
            curr.next = list2
        else:
            curr.next = list1

        return merged.next