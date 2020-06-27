found = False
while x and not found:
    if match(x[o]):
        print('Ni')
        found = True
    else x = x[1:]
if not found:
    print('not found')