class Solution:
    def maxProfit(self, prices):
        b = s = p = 0
        for i in range(len(prices)-1):
            s+= 1
            if prices[s] - prices[b] > 0:
                p += prices[s] - prices[b]
            b+=1
        return p

s = Solution()
s.maxProfit([6,1,3,2,4,7])
#            b
#             