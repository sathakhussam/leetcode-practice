class Solution:
    def longestCommonPrefix(self, strs):
        pr = strs[0]
        for word in strs[1:]:
            s = -1
            for i in range(min(len(pr), len(word))):
                if i == 0 and pr[i] == word[i]:
                    s = 0
                if i != 0 and s == i-1 and pr[i] == word[i]:
                    s += 1
            pr = pr[:s+1]
        return pr

s = Solution()
s.longestCommonPrefix(["flower","flow","flight"])