class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n_gap = numRows - 1 if numRows > 2 else 0
        letter_cols = [[""] * numRows]
        nl = len(s)
        mc = 1
        while nl > 0:
            if n_gap == 0 or (mc - 1) % n_gap == 0: 
                i = 0
                for letter in s[len(s)-nl:len(s)-nl+numRows]:
                    letter_cols[mc-1][i] = letter
                    i+=1
                nl = nl - numRows
            else:
                i = numRows - ((mc - 1) % n_gap) - 1
                letter_cols[mc-1][i] = s[len(s)-nl]
                nl -= 1
            mc += 1
            letter_cols.append([""]*numRows)
        letter_cols.pop()
        final = ""
        for colIndex in range(numRows):
            final = final +"".join([letters[colIndex] for letters in letter_cols])
        return final
            
s = Solution()
# s.convert("PAYPALISHIRING", 4)
s.convert("A", 1)

