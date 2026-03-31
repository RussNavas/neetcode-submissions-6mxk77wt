class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freq = {}

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1

        print(freq)

        for key in freq:
            if freq[key] > 1:
                return True
   
        return False

         