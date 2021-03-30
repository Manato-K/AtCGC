import os

i = 0
while i < 100:
    i += 1
    s = "AtCGC_{0}.py".format(i)
    print(s)
    path = './{0}'.format(s)
    f = open(path, 'w')
    f.write('')
