L = []
#for i in range(6): L.append(2**i)
#L = list(map(lambda x : 2**x, (range(7))))
L = [2**i for i in  range(7)]
X = 5
found = False 
i = 0

pow_two = 2**X
'''
while i < len(L):
    if pow_two != L[i]: 
        i = i+1 
        print(X, 'not found')   
else: 
    print('at index', i)
'''    

#if 2**X in L: print('at index', L.index(2**X))

for i in range(len(L)):
    if not 2**i in L:
        print (X, 'not found')
else:
    print('at index', L.index(pow_two))