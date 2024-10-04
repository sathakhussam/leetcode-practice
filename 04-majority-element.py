import math

class Solution:
    def majorityElement(self, nums):
        m = math.ceil(len(nums)/2)
        k = {}
        for n in nums:
            if n not in k:
                k[n] = 1
                if k[n] == m:
                    return n
            else:
                k[n] = k[n] +1
                if k[n] == m:
                    return n
s = Solution()

s.majorityElement([3,2,3])