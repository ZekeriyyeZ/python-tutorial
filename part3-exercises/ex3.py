ages = {'Rufat' : 29, 'Parvin' : 27, 'Zeki' : 20}
l = [keys for keys in ages]
l.sort()

for i in range(len(l)):
    print(l[i] + " =>", ages[l[i]], end = '\n')
