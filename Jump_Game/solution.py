class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #My solution 
        # if(len(nums)<=1):
        #     return True
        # p1 = len(nums)-1
        # inc = 1
        # while(p1>=0):
        #     if(nums[p1-inc]>=inc):
        #         if p1-inc==0:
        #             return True
        #         p1-=inc
        #         inc=1
        #     else:
        #         if p1-inc==0 and nums[p1-inc]<inc:
        #             return False
        #         inc+=1
            
        # return True
        #Greedy Approach
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i]>=goal:
                goal = i
        return True if goal == 0 else False

            
            
                