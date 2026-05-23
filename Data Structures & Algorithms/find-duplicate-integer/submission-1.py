class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            pos = abs(nums[i]) - 1
            nums[pos] *= -1
            print("nums[pos]:", nums[pos], "i:", i) 
            if nums[pos] > 0:
                return abs(nums[i]) 