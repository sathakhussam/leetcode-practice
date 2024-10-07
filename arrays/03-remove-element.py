class Solution:
    def removeElement(self, nums, val):
        k = len(nums) -1
        for i in range(k, -1, -1):
            if nums[i] == val:
                nums[i] = nums[k] 
                k=k - 1
        return k+1
            

s = Solution()

s.removeElement([3,2,3, 1,2,3], 3)