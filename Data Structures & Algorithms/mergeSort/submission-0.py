# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._helper(pairs, 0, len(pairs)-1)

    # merge
    def merge(self, arr, start, mid, end):
        left = arr[start:mid+1]
        right = arr[mid+1:end+1]

        i = 0
        j = 0
        k = start

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


    # helper
    def _helper(self, arr, start, end):

        if (end - start)+1 <= 1:
            return arr

        mid = (end + start) // 2

        # go left
        self._helper(arr, start, mid)

        # go right
        self._helper(arr, mid+1, end)

        # merge
        self.merge(arr, start, mid, end)

        return arr
