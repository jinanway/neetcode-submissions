class Solution:
    def isPalindrome(self, x: int) -> bool:
       nums = str(x)
       l = 0
       r = len(nums) - 1
       
       while(l < r):
            if(nums[l] != nums[r]):
                return False
            l += 1
            r -= 1


       return True








         

        