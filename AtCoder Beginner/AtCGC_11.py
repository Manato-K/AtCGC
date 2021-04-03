n = int(input())

t0, x0, y0, = 0, 0, 0

for i in range(n):
    t1, x1, y1 = map(int, input().split())
    t = t1 - t0
    dist = abs(x1 - x0) + abs(y1 - y0)
    if t >= dist and (t % 2) - (dist % 2) == 0:
        ans = 'YES'
        t0, x0, y0, = t1, x1, y1
    else:
        ans = 'NO'
        break

print(ans)