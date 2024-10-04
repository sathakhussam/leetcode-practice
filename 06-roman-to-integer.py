# class Solution:
#     def romanToInt(self, s):
#         rules = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000,
#         }
#         c = 0
#         p = None
#         for letter in s:
#             value = rules[letter]
#             if p == None or p >= value:
#                 p = value
#                 c += p
#             if p < value:
#                 c -= p*2
#                 p = value
#                 c += p
#             # print(c)
#         # print(c)
#         return c
class Solution:
    def romanToInt(self, s):
        rules = {
            "I": 1,
            "V": 5,
            "IV": 4,
            "X": 10,
            "IX": 9,
            "L": 50,
            "XL": 40,
            "C": 100,
            "XC": 90,
            "D": 500,
            "CD": 400,
            "M": 1000,
            "CM": 900,
        }
        c = 0
        
        
        for i in range(len(s)-1, -1, -2):
            letters = s[i-1:i+1] if i-1 >= 0 else s[0]
            print(letters)
            if letters in rules:
                c += rules[letters]
            else:
                for l in letters:
                    c += rules[l]
            print(c)
        print(c)
        return c

# TWO LETTERS AT A TIME

s = Solution()
s.romanToInt("MCDLXXVI")