import "maps"
func isAnagram(s string, t string) bool {
    sMap := freqMap(s)
    tMap := freqMap(t)
    return maps.Equal(sMap, tMap)
}

func freqMap (s string) map[rune]int{
    fMap := make(map[rune]int)
    for _, c := range s{
        if _, ok := fMap[c]; ok{
            fMap[c]++
        }else{
            fMap[c] = 1
        }
    }
    return fMap
}
