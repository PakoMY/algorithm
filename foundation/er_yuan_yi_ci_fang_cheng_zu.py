cx, cy, c = [0] * 2, [0] * 2, [0] * 2
for i in range(0, 4):
    s = input().split(' ')
    d = -1 if i % 2 else 1
    for ss in s:
        if 'x' in ss:
            if len(ss) == 1:
                cx[i // 2] += d
            elif len(ss) == 2 and ss[0] == '-':
                cx[i // 2] -= d
            else:
                cx[i // 2] += eval(ss[:-1]) * d
        elif 'y' in ss:
            if len(ss) == 1:
                cy[i // 2] += d
            elif len(ss) == 2 and ss[0] == '-':
                cy[i // 2] -= d
            else:
                cy[i // 2] += eval(ss[:-1]) * d
        else:
            c[i // 2] += eval(ss) * d


x, y, r = 0, 0, 0
if cx[0] * cx[1] == 0:
    rx = cx[0] * cy[1] - cx[1] * cy[0]
    r = c[0] * cy[1] - c[1] * cy[0]
    x = -r / rx
    y = -(cx[0] * x + c[0]) / cy[0]
else:
    ry = cy[0] * cx[1] - cy[1] * cx[0]
    r = c[0] * cx[1] - c[1] * cx[0]
    y = -r / ry
    x = -(cy[0] * y + c[0]) / cx[0]

print(str(round(x, 1)) + ' ' + str(round(y, 1)))
