a = input()
a = eval(a)
b = [i for i in range(0, 1000002)]
for i in range(1, 1000002):
    b[i] = 0
for i in range(a):
    p = input()
    o = p.split(' ')
    l = eval(o[0])
    r = eval(o[1])
    r -= 1
    b[l] = b[l] + 1
    b[r + 1] = b[r + 1] - 1
now = 0
ans = 0
if b[0] > 0:
    now = 1
ans = now
for i in range(1, 1000001):
    b[i] = b[i] + b[i - 1]
    if b[i] == 0:
        now = 0
    else:
        now = now + 1
    ans = max(ans, now)
print(ans)
