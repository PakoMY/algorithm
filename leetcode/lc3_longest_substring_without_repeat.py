def lengthOfLongestSubstring(s):
    s = list(s)
    n = len(s)
    sub = set([])
    ans = i = j = 0
    while i < n and j < n:
        if not s[j] in sub:
            sub.add(s[j])
            j += 1
            ans = max(ans, j - i)
        else:
            sub.remove(s[i])
            i += 1
    return ans

#解法2 hashmap
def lengthOfLongestSubstring2(s):
    s = list(s)
    n = len(s)
    ans = 0
    map = {}
    i = 0
    for j in range(n):
        if s[j] in map.keys():
            i = max(map.get(s[j]), i)
        ans = max(ans, j - i + 1)
        map[s[j]] = j + 1
    return ans

lengthOfLongestSubstring2('abca')
