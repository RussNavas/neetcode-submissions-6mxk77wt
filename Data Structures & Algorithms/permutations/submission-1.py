class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(candidate, used):
            # base case: candidate has all the nums in it
            if len(candidate) == len(nums):
                res.append(candidate[:])
                return

            # go through all the numbers:
            for num in nums:
                if num not in used:
                    candidate.append(num)
                    used.add(num)
                    backtrack(candidate, used)
                    candidate.pop()
                    used.remove(num)

        backtrack([], set())
        return res
        