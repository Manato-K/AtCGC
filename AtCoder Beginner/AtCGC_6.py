N, A, B = map(int, input().split())
cnt = 0
for i in range(N+1):
    n = i
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    if A <= sum <= B:
        cnt += i
print(cnt)