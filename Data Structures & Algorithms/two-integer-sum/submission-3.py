class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # value : index

        for index, value in enumerate(nums):
            complement = target - value
            if complement in prevMap:
                return [prevMap[complement], index]
            elif value not in prevMap:
                prevMap[value] = index






        