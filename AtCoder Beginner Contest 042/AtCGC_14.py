n, k = map(int, input().split())
d = list(input().split())

flag = True

while flag:
    for i in range(k):
        if d[i] in str(n):
            n = str(int(n) + 1)
            break
        else:
            continue
    else:
        flag = False
print(n)