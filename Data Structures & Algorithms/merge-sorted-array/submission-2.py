class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        k = 0
        i = 0
        j = 0
        nums1_cpy = nums1[:m]

        while k <= (m + n) and i < m and j < n:
            if nums1_cpy[i] < nums2[j]:
                nums1[k] = nums1_cpy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        while i < len(nums1_cpy):
            nums1[k] = nums1_cpy[i]
            i += 1
            k += 1
        while j < len(nums2):
            nums1[k] = nums2[j]
            j += 1
            k += 1
        