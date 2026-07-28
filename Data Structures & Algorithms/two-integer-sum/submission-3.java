class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i = 0;
        int j = 1;
        boolean check = false;
        int[] indices = new int[2];
        while(i < nums.length && j < nums.length && check == false){
            if(nums[i] + nums[j] == target){
                check = true;
            } else{
                j++;
                if(j == nums.length){
                    i++;
                    j = i+1;
                }
            }
            System.out.println(check);
        }
        indices[0] = i;
        indices[1] = j;
        return indices;
    }
}
