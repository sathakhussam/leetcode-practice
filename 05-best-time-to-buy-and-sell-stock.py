class Solution:
    def maxProfit(self, prices):
        b = s = p = None
        p = 0
        for i in range(len(prices)):
            price = prices[i]
            if b == None or b > price:
                b = price
                s = prices[i]
                p = max(p, s-b) 
            else:
                s = price
                p = max(p, s-b) 
        return p

s = Solution()

# s.maxProfit([7,1,5,3,6,4])
s.maxProfit([2,1,2,1,0,1,2])