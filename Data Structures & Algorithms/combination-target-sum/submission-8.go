func combinationSum(nums []int, target int) [][]int {
    res := [][]int{}
    cur := []int{}
    total := 0

    var dfs func(int)
    dfs = func(i int){
        if total == target{
            temp := make([]int, len(cur))
            copy(temp, cur)
            res = append(res, temp)
            return
        }

        if total > target || i == len(nums){
            return
        }

        total += nums[i]
        cur = append(cur, nums[i])
        dfs(i)
        total -= nums[i]
        cur = cur[:len(cur)-1]
        dfs(i+1)
        return
    }
    dfs(0)
    return res
}
