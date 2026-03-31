# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._helper(pairs, 0, len(pairs))

    def _helper(self, pairs, start, end):
        # base case
        if (end - start) + 1 <= 1:
            return pairs

        #mid
        mid = start + (end - start) // 2
        #left
        self._helper(pairs, start, mid) 
        #right
        self._helper(pairs, mid+1, end)
        #merge
        self.merge(pairs, start, mid, end)
        return pairs

    def merge(self, pairs, start, mid, end):
        l1= pairs[start:mid+1]
        l2 = pairs[mid+1:end+1]
        i = 0
        j = 0
        k = start

        while i < len(l1) and j < len(l2):
            if l1[i].key <= l2[j].key:
                pairs[k] = l1[i]
                i += 1

            else:
                pairs[k] = l2[j]
                j += 1

            k += 1

        while i < len(l1):
            pairs[k] = l1[i]
            i += 1
            k += 1

        while j < len(l2):
            pairs[k] = l2[j]
            j += 1
            k += 1



