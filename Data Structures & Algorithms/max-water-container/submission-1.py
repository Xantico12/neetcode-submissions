class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        waterMax = 0

        for i in range(0, len(heights) - 1):
            for j in range(i + 1, len(heights)):
                waterCurrent = min(heights[i], heights[j]) * (j - i)
                if waterCurrent > waterMax:
                    waterMax = waterCurrent
        return waterMax