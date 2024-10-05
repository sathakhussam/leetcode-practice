class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        l = nums[(len(nums) - k):]
        r = nums[:(len(nums) - k)]
        for i in range(len(nums)):
            if len(l) > i:
                nums[i] = l[i]
            else:
                nums[i] = r[i- len(l)]
        print(nums)

s = Solution()
s.rotate([1,2,3,4,5,6,7], 3)
s.rotate([-1, 100, 3, 99], 5)