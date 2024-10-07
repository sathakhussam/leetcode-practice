class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        tg = 0
        tc = 0
        s = 0
        g = 0

        for i in range(len(gas)):
            tg += gas[i]
            tc += cost[i]
            g += gas[i]
            g -= cost[i]
            if g < 0:
                s = i + 1
                g = 0

        if tg < tc:
            return -1
        return s

        
s = Solution()
s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
# s.canCompleteCircuit([1,2,0,3,4, 0,5], [3,4,0,5,1,0,2])
# s.canCompleteCircuit([2],[2])