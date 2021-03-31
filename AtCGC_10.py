s = input()
words = ["erase", "dream", "eraser", "dreamer"]
for word in words:
    s = s.replace(word, '')
if len(s) == 0:
    print('YES')
else:
    print('NO')