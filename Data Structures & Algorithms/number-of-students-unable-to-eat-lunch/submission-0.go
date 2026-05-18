func countStudents(students []int, sandwiches []int) int {
    res := len(students)
    cnt := make([]int, 2)
    for _, student := range students{
        cnt[student]++
    }

    for _, s := range sandwiches{
        if cnt[s] > 0 {
            cnt[s]--
            res--
        }else{
            break
        }
    }
    return res
}