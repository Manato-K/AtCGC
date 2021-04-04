s = list(str(input()))
ans = ''
for i in s:
    if i != 'B':
        ans += str(i)
    else:
        ans = ans[:-1]

print(ans)