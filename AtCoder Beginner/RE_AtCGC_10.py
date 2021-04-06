s = input()
words = ['eraser', 'erase', 'dreamer', 'dream']
for word in words:
    s = s.replace(word, '')
if len(s) == 0:
    print('YES')
else:
    print('NO')