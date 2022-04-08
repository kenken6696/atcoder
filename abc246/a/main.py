#!/usr/bin/env python3

x = list()
y = list()
for i in range(3):
    xi, yi = list(map(int, input().split()))
    x.append(xi)
    y.append(yi)

ux = set(x)
uy = set(y)
x_t, y_t = x[0], y[0]
x_y, y_y = 0,0
x_t_c, y_t_c, x_y_c, y_y_c = 1,1,0,0
for i in range(0,3):
    if x_t == x[i]:
        x_t_c += 1
    else:
        x_y_c += 1
        x_y = x[i]
    if y_t == y[i]:
        y_t_c += 1
    else:
        y_y_c += 1
        y_y = y[i]

ans = [0,0]
if x_t_c == 2:
    ans[0] = x_t
else:
    ans[0] = x_y
if y_t_c == 2:
    ans[1] = y_t
else:
    ans[1] = y_y

print(*ans)


