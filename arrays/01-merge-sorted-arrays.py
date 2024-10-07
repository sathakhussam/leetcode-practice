class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            elif nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        if j >= 0:
            ns = nums2[0:j+1]
            for num in ns[::-1]:
                nums1[k] = num
                j -= 1
                k -= 1
            
ss = Solution()
ss.merge([4,5,6,0,0,0], 3, [1,2,3],3)
