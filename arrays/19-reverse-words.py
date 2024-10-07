class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        s.strip()
        for word in s.split(" "):
            words.append(word) if word else None
        print(words)
        i = 0
        j = len(words) - 1
        while i < j:
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1
        print(words)

s = Solution()
s.reverseWords("  the  sky     is   blue")