class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # temp, index
        track = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                track[stackInd] = ( i - stackInd)
            stack.append([temp, i])
        return track


        