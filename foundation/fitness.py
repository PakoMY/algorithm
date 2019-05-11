"""
健身
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
小王是一个喜欢健身的人，他每天都会围着一个n*n的场地外侧跑步，他是一个有强迫症的人，
每跑(n+1)个单位长度，他就要在地上做一个标记，当他在一个点重复标记的时候，
他就会结束一天的锻炼，显然当n一定时，他每天打标记的数量也是一定的，请你计算出来他每天打多少个标记。(最后一次重复标记也要计数)
"""

import sys

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

t = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))

for value in a:
    print(((4 * value ) // gcd(4 * value, value + 1)) + 1)
