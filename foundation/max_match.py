"""
最多匹配
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
给出一个仅由大小写字母和‘？’组成的字符串S，和一个仅由大小写字母组成的字符串T，
已知‘？’可以由任何一个大小写字母替代，问S字符串最多可以匹配多少个T字符串，
两个不同的匹配之间可以重合，例如S=ababa，T=aba，则S最多同时匹配两个T串。

import sys
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

ans = 0
for i in range(len(s) - len(t) + 1):
    j = 0
    while j < len(t):
        if s[i+j] == "?":
            j += 1
            continue
        if t[j] == s[i + j]:
            j += 1
            continue
        break
    if j >= len(t):
        ans += 1
print(ans)
"""
import sys
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

nxt = [0] * (len(t) + 1)
for i in range(len(t)):
    j = i
    while j > 0:
        j = nxt[j]
        if t[i] == t[j]:
            nxt[i + 1] = j + 1
            break

state = [-1] * len(t)
state[0] = 0
for c in s:
    new_state = [-1] * len(t)
    new_state[0] = 0
    for j in range(len(t)):
        if state[j] == -1:
            continue
        if c == t[j] or c == '?':
            nj = j + 1
            ntimes = state[j]
            if nj >= len(t):
                nj = nxt[nj]
                ntimes += 1
            new_state[nj] = max(state[nj], ntimes)
        if c != t[j] or c == '?':
            nj = nxt[j]
            ntimes = state[j]
            new_state[nj] = max(state[nj], ntimes)
    state = new_state
print(max(state + [0]))
