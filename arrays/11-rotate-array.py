class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        l = 0
        r = len(nums) -1
        while l <r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        l = 0
        r = k -1
        print(l, r)
        while l <r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        l = k
        r = len(nums) - 1
        print(l, r)
        while l <r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        print(nums)
s = Solution()
s.rotate([1,2,3,4,5,6,7], 3)
# s.rotate([-1, 100, 3, 99], 3)
s.rotate([1,2,3,4,5], 3)