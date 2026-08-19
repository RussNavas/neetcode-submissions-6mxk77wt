class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        hashMap = {
            "2":"abc", "3":"def",
            "4":"ghi", "5":"jkl", "6":"mno",
            "7":"pqrs", "8":"tuv", "9":"wxyz"
        }

        res = []
        def backtrack(path, idx):
            if idx == len(digits):
                res.append(path)
                return
            
            for letter in hashMap[digits[idx]]:
                backtrack(path + letter, idx + 1)
        backtrack("", 0)
        return res