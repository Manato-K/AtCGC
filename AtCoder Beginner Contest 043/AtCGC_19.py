s = list(input())
n = len(s)

ans = [-1, -1]
if n == 2:
    if s[0] == s[1]:
        ans = [1, 2]
else:
    for i in range(n - 2):
        if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i + 2] == s[i]:
            ans = [i + 1, i + 3]
            break
print(ans[0], ans[1])