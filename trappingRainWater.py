class Solution:
    def trap(self, height: List[int]) -> int:
        leftIndex = 0
        trapped = 0
        total = 0
        max_value = max(height)  # Find the maximum value in the list
        last_index = len(height) - 1 - height[::-1].index(max_value)  # Find the last occurrence of the max value
        for i in range(last_index):
            if height[i] > 0 and leftIndex == 0:
                leftIndex = height[i]
            elif height[i] == leftIndex:
                total += trapped
                trapped = 0
            elif height[i] > leftIndex:
                total += trapped
                trapped = 0
                leftIndex = height[i]
            elif height[i] < leftIndex:
                trapped += leftIndex - height[i]
        total += trapped
        trapped = 0
        leftIndex = 0

        for i in range(len(height) - 1, last_index, -1):
            if height[i] > 0 and leftIndex == 0:
                leftIndex = height[i]
            elif height[i] == leftIndex:
                total += trapped
                trapped = 0
            elif height[i] > leftIndex:
                total += trapped
                trapped = 0
                leftIndex = height[i]
            elif height[i] < leftIndex:
                trapped += leftIndex - height[i]

        total += trapped

        return total