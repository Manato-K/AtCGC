import os
i = 0
while i < 10:
    i += 1
    s = "RE_AtCGC_{0}.py".format(i)
    print(s)
    path = './{0}'.format(s)
    f = open(path, 'w')
    f.write('')