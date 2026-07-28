/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }

        ArrayList<Integer> nums = new ArrayList<>();
        
        while(head.next != null){
            nums.add(head.val);
            head = head.next;
        }

        Collections.reverse(nums);
        ListNode curr = new ListNode(nums.get(0));
        head.next = curr;
        for(int i = 1; i < nums.size(); i++){
            curr.next = new ListNode(nums.get(i));
            curr = curr.next;
        }

        return head;
    }
}
