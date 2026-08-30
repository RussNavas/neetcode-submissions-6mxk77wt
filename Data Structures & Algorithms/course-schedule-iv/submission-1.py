class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}
        for pre, crs in prerequisites:
            adj[crs].append(pre)
        
        prereq = {} # crs : set() of prereqs includes indirect
        def dfs(crs):
            if crs not in prereq:
                prereq[crs] = set()
                for pre in adj[crs]:
                    prereq[crs] |= dfs(pre)
                prereq[crs].add(crs)
            return prereq[crs]
        
        for crs in adj:
            dfs(crs)

        res = []
        for u, v in  queries:
            res.append(u in prereq[v])
        return res