func subsets(nums []int) [][]int {
    res := [][]int{}
    cur := []int{}

    dfs(0, len(nums), &res, cur, nums)
    return res
}

func dfs(i, j int, res *[][]int, cur, nums []int){

    if i == j{
        temp := make([]int, len(cur))
        copy(temp, cur)
        *res = append(*res, temp)
        return
    }

    cur = append(cur, nums[i])
    dfs(i+1, j, res, cur, nums)
    cur = cur[:len(cur)-1]
    dfs(i+1, j, res, cur, nums)
    return
}
