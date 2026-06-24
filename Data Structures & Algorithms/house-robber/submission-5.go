func rob(nums []int) int {

	n := len(nums)
	memo := make([]int, n+1)
	for i := 0; i <= n; i++{
		memo[i] = -1
	}
    
	var dfs func(int) int
	dfs = func(i int) int {
		if i >= len(nums){
			return 0
		}

		if memo[i] != -1 {
			return memo[i]
		}

		memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
		return memo[i]
	}

	return dfs(0)
}
