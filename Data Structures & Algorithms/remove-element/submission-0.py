class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # start at the head
        k = 0
        # check all indices in the array
        for i in range(len(nums)):
            # if the element at that position is valid
            if nums[i] != val:
                # move it to front and move the ptr
                nums[k] = nums[i]
                k += 1
        return k # the ptr is also a counter of valid elements