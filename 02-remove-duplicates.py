class Solution:
    def removeDuplicates(self, nums):
        k = 0
        for i in range(len(nums)):
            if nums[k] != nums[i]:
                if k+1 == i:
                    k = k+1
                else:
                    nums[k+1] = nums[i]
                    k = k+1
        return k+1
                

s = Solution()
s.removeDuplicates([1,1,2,3,4,4,5])