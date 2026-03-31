class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for n in nums:
            if n not in hashMap:
                hashMap[n] = 1
            else:
                return True
        return False