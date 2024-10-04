class Solution:
    def strStr(self, haystack, needle):
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i: i+len(needle)] ==  needle:
                    return i
        return -1


s = Solution()
print(s.strStr("sadbutsad", "sadd"))