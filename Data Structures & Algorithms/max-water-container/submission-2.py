class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        waterMax = min(heights[l], heights[r]) * (r - l)

        while l < r:
            waterCurrent = min(heights[l], heights[r]) * (r - l)
            
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            elif heights[l] == heights[r]:
                l += 1
                r -= 1

            if waterCurrent > waterMax:
                waterMax = waterCurrent
        return waterMax