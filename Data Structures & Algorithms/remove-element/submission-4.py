class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # remove all occurrences of val in place
        # order of ele doesnt matter
        # ignore k+1 ele
        # first k must be non val

        # consider a pointer to demark valid position
        # overrwite that spot with first non val val encountered
        # inc ptr fwd and return that value

        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l