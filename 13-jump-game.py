# class Solution:
#     def canJump(self, nums):
#         memory = [False] * len(nums)
#         memory[-1] = True

#         for i in range(len(nums)-2,-1,-1):
#             num = nums[i]
#             if  (num > 0 and memory[i+1] == True)or num >= len(nums) - 1 - i:
#                 memory[i] = True
#             if memory[i] == False:
#                 mem = [False] * num
#                 for j in range(0, len(mem)):
#                     if i+j+1 < len(memory):
#                         mem[j]  = memory[i+j+1]
#                 memory[i] = any([memory[i], any(mem)])
#         return memory[0]

class Solution:
    def canJump(self, nums):
        memory = [False] * len(nums)  # Memory to track if a position can reach the end
        memory[-1] = True  # The last position is always reachable from itself

        for i in range(len(nums) - 2, -1, -1):
            num = nums[i]
            # If a jump can directly reach the end or the next step is valid
            if num > 0 and memory[i + 1] == True or num >= len(nums) - 1 - i:
                memory[i] = True
            else:
                # Check if it's possible to reach the end within the next few steps
                for j in range(1, num + 1):  # Jump within the range allowed by nums[i]
                    if i + j < len(memory) and memory[i + j] == True:
                        memory[i] = True
                        break  # No need to check further once we find a valid jump

        return memory[0]  # Return whether the first position can reach the end

s = Solution()
s.canJump([3,0,8,2,0,0,1])