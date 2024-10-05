

class Solution:
    def intToRoman(self, num: int) -> str:
        rules = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        rules_in = [1,4,5,9,10,40,50,90,100,400,500,900,1000, 10000]
        i = -1
        final = ""
        for l in str(num)[::-1]:
            i += 1 
            v = int(l+ ("0" * i)) 
            # print(v)
            if v in rules:
                final = rules[v]+ final
                print(final)
            else:
                tf = ""
                while v > 0:
                    first_val = None
                    for j in range(len(rules_in)):
                        if v < rules_in[j]:
                            first_val = rules_in[j -1]
                            break
                        if v == rules_in[j]:
                            first_val = rules_in[j]
                            break
                    tf = tf+ rules[first_val]
                    v -= first_val
                final = tf + final
        print(final)
        return final

s = Solution()
s.intToRoman(3749)