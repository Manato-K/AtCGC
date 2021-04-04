n = int(input())
a = list(map(int, input().split()))
x = 0
cnt = 0
while x == 0:
    for i in range(n):
        if a[i] % 2 == 0:
            print(cnt)
            x = 1
            break
        else:
            s[i] /= 2
    cnt += 1
