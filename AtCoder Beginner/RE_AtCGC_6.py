n, a, b = map(int, input().split())
cnt = 0
for i in range(n+1):
    n = i
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    if a <= sum <= b:
        cnt += i
print(cnt)