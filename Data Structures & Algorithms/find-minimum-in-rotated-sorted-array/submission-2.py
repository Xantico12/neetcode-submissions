class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        if n == 1 or nums[r] > nums[l]:
            return nums[0]
        
        while l <= r:
            mid = (r + l) // 2

            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            elif nums[mid] < nums[r]:
                r = mid - 1
            
            else:
                l = mid + 1
        
        

            
# [1, 2, 3, 4, 5, 6]

# [6, 1, 2, 3, 4, 5]

# [5, 6, 1, 2, 3, 4]

# [4, 5, 6, 1, 2, 3]

# [3, 4, 5, 6, 1, 2]

# [2, 3, 4, 5, 6, 1]