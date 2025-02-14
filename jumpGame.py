from typing import List

# Provided class
class Solution:
    def jump(self, nums: List[int]) -> int:
        counter = 0  # Tracks current jump position   
        current = nums[counter]
        jumpCount = 1
        jumpList = [0] * len(nums)

        if len(nums) == 1:
            return 0
        
        while True:
            maxIndex = current + counter + 1
            if maxIndex > len(nums):
                maxIndex = len(nums)
            for i in range(counter + 1, maxIndex):
                if counter + 1 < jumpList[i] or jumpList[i] == 0:
                    # jumpList[i] = jumpList[i] + 1
                    # jumpList[i] += jumpCount
                    jumpList[i] += jumpList[counter] + 1
                    # print(jumpList)
                    # print(counter)

            if jumpList[len(nums)-1] != 0:
                return jumpList[len(nums)-1]

            counter += 1
            jumpCount += 1
            current = nums[counter]

# nums = [2, 3, 1, 1, 4]
nums = [2, 4, 4, 2, 2, 2, 5]

# Creating an instance of the Solution class
solution = Solution()

# Running the test case
result = solution.jump(nums)
print(f"Result: {result}")
