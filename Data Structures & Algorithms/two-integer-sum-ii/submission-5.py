class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(numbers)):
            if numbers[i] not in hashMap:
                hashMap[numbers[i]] = i

        for i in range(len(numbers)):
            cur = numbers[i]
            comp = target - cur
            if comp in hashMap and hashMap[comp] != i:
                return [min(i, hashMap[comp])+1, max(i, hashMap[comp])+1]