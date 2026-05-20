class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = nums1[:m]
        i = j = k = 0
        while k < m + n:
            if j >= n or ( i < m and tmp[i] <= nums2[j]):
                nums1[k] = tmp[i]
                i+= 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        