func isValid(s string) bool {
    
    stack := []rune{}
    var closeToOpen = map[rune]rune{}
    closeToOpen = map[rune]rune{
            ')': '(',
            ']': '[',
            '}': '{',
        }
    // iterate through each char in s
    for _, c := range s {
        if open, exists := closeToOpen[c]; exists{
            // valid char so check if it is on top of stack
            if len(stack) > 0 && stack[len(stack)-1] == open{
                // it is so pop it
                stack = stack[:len(stack)-1]
            } else {
                return false
            }
        } else {
            stack = append(stack, c)
        }
    }
    return len(stack) == 0

}
