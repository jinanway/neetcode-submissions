class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        trips = []

        if(len(nums) == 3):
            if(nums[0] + nums[1] + nums[2] == 0):
                trips.append([nums[0], nums[1], nums[2]])

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while(l < r):
                if(nums[l] + nums[r] + nums[i] == 0 and
                [nums[i], nums[l], nums[r]] not in trips):
                    trips.append([nums[i], nums[l], nums[r]])
                elif(nums[l] + nums[r] + nums[i] > 0):
                    r -= 1
                else:
                    l += 1
                
            
        
        return trips