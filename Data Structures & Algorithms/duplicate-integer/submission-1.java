class Solution {
    public boolean hasDuplicate(int[] nums) {
        Arrays.sort(nums);

        int l = 0;
        int r = 1;
        boolean check = false;
        while(l < nums.length && r < nums.length && !check){
            if(nums[l] == nums[r]){
                check = true;
            }else{
                l++;
                r++;                
            }
        }
        return check;
    }
}
