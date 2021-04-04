N = int(input())
a = list(map(int, input().split()))
cnt = 0
x = 0

while x == 0:
    for i in range(N):
        if a[i] % 2 == 1:
            print(cnt)
            x = 1
            break
        else:
            a[i] /= 2
    cnt += 1