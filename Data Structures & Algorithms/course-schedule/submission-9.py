class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = {i: [] for i in range(numCourses)}
        visited = set()

        for crs, pre in prerequisites:
            prereq_map[crs].append(pre)

        def dfs(crs):
            if prereq_map[crs] == []:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for n in prereq_map[crs]:
                if not dfs(n):
                    return False
            visited.remove(crs)
            prereq_map[crs] = []
            return True
        
        for n in range(numCourses):
            res = dfs(n)
            if not res:
                return False
        return True