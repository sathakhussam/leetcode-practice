import math

# class Solution:
#     def majorityElement(self, nums):
#         m = math.ceil(len(nums)/2)
#         k = {}
#         for n in nums:
#             if n not in k:
#                 k[n] = 1
#                 if k[n] == m:
#                     return n
#             else:
#                 k[n] = k[n] +1
#                 if k[n] == m:
#                     return n

class Solution:
    def majorityElement(self, nums):
        res = majority = 0
        
        for n in nums:
            if majority == 0:
                res = n
            
            majority += 1 if n == res else -1
        
        return res

s = Solution()

s.majorityElement([3,2,1,3])