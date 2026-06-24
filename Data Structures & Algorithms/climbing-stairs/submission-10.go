func climbStairs(n int) int {
    
    cache :=  make(map[int]int)

    for i := 0; i <= n ; i++{

        if i <= 2 {
            cache[i] = i
            continue
        }
        if num, ok := cache[i-1]; ok {
            if num2, ok := cache[i-2]; ok {
                cache[i] = num + num2
                continue
            }
        }
    }
    return cache[n]
}
