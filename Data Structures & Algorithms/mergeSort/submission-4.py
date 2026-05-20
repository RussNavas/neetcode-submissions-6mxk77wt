# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._mergeSort(pairs, 0, len(pairs)-1)

    def _mergeSort(self, arr, s, e):
        if ((e-s+1) <= 1):
            return arr

        m = (e+s)//2
        self._mergeSort(arr, s, m)
        self._mergeSort(arr, m+1, e)
        self.merge(arr, s, m, e)
        return arr

    def merge(self, arr, s, m, e):
        L = arr[s:m + 1]
        R = arr[m + 1:e+1]
        i = 0
        j = 0
        k = s

        while i < len(L) and j < len(R) and k < len(arr):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
