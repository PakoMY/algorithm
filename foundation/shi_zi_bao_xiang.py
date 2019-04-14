
##dp[i][j]  i 表示遍历到第i个宝箱  j 有两个值 0表示取 1表示不取
def solve(tmp, l, r):
    ans = 0
    arr = tmp[l:r]
    dp = [[0] * 2 for i in range(0, len(arr))]
    dp[0][1] = arr[0]
    for i in range(1, len(arr)):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = dp[i - 1][0] + arr[i]
    return max(dp[-1][0], dp[-1][1])


def solve1():
    ans = a[x]
    if x - 1 > 0:
        ans += solve(a, 0, x - 1)
    if x + 2 < len(a):
        ans += solve(a, x + 2, len(a))
    if y - 1 > 0:
        ans += solve(b, 0, y - 1)
    if y + 2 < len(b):
        ans += solve(b, y + 2, len(b))
    return ans


def solve2():
    ans = 0
    if x > 0:
        ans += solve(a, 0, x)
    if x + 1 < len(a):
        ans += solve(a, x + 1, len(a))
    if y > 0:
        ans += solve(b, 0, y)
    if y + 1 < len(b):
        ans += solve(b, y + 1, len(b))
    return ans


arr1 = [eval(x) for x in input().split(' ')]
n = arr1[0]
a = arr1[1:]

arr2 = [eval(x) for x in input().split(' ')]
m = arr2[0]
b = arr2[1:]


cnt, x, y = [eval(x) for x in input().split(' ')]

print(max(solve1(), solve2()))
