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
            crs_to_pre[crs] = []
            visited.remove(crs)
            return True
        
        for crs in crs_to_pre:
            if not dfs(crs):
                return False
        return True