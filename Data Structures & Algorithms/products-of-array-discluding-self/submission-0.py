class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        product = 1

        prefix = suffix = exceptSelf = []

        for i in range(len(nums)):
            prefix = nums[:i]
            suffix = nums[i+1:]

            exceptSelf = prefix + suffix

            for num in exceptSelf:
                product *= num
            
            output[i] = product
            product = 1

        return output
            