a = int(input())
b = int(input())
c = int(input())
x = int(input())
cnt = 0
for a in range(a+1):
    for b in range(b+1):
        for c in range(c+1):
            if 500 * a + 100 * b + 50 * c == x:
                cnt += 1
print(cnt)