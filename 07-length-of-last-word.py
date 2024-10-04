class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        return len(s.split(" ")[-1])

s = Solution()
s.lengthOfLastWord("Hello World")