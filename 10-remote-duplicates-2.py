class Solution:
    def removeDuplicates(self, nums):
        l = 0
        c = 0
        p = None
        for r in range(0, len(nums)):
            if p == None or p == nums[r]:
                p = nums[r]
                c += 1
            else:
                c = 1
                p = nums[r]
            if c <= 2:
                nums[l] = p
                l += 1
        return l

s = Solution()
s.removeDuplicates([1,1,1,2,2,2,3])