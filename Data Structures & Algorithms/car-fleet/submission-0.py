class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [[p,s] for p,s in zip(position, speed)]
        stack = []

        for p,s in sorted(ps)[::-1]: # iter array bckwd sorted far to close
            t = (target-p)/s
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # check if bottle neck
                stack.pop() # only need one to rep the fleet
        return len(stack)

        