class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crs_to_pre = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            crs_to_pre[crs].append(pre)

        visited = set()

        def dfs(crs):

            if crs in visited:
                return False

            if crs_to_pre[crs] == []:
                return True

            visited.add(crs)
            for pre in crs_to_pre[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            crs_to_pre[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
