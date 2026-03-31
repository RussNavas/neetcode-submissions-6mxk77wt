class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        l = 0
        r = 0

        product = None

        while l < len(nums):
            while r < len(nums):
                if l != r:
                    if product == None:
                        product = nums[r]
                        r += 1
                    else:
                        product *= nums[r]
                        r += 1
                else:
                    r += 1
            output.append(product)
            l += 1
            r = 0
            product = None
        return output


 
            

        