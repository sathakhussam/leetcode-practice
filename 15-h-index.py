class Solution:
    def hIndex(self, citations):
        h_index = [0]
        for h in range(1, len(citations)+1):
            no_of_times_present = 0
            if h_index[-1] != h-1:
                break
            for num in citations:
                if num >= h:
                    no_of_times_present += 1
                if no_of_times_present >= h:
                    h_index.append(h)
                    break
        # print(h_index)
        return h_index[-1]

s = Solution()
s.hIndex([1])