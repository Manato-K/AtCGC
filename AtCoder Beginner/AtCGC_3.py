s1s2s3 = int(input())
s1 = s1s2s3 % 10
s2 = int(s1s2s3/10) % 10
s3 = int(s1s2s3/100)
total = s1 + s2 + s3
print(total)