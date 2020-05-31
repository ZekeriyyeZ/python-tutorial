"""
Chapter 7 syntax recap in one example
"""

s = "zekiNilirufetZekiniliRufetrufetTefurikezteFur"
ctr = 0
s = s.lower()
wanted = 'rufet'

for i in range(0, len(s)):
    if s[i:i+5] == wanted or s[i+4:i-1:-1] == wanted: 
        ctr+=1
        
s = ('\nThere is ' + str(ctr) + ' copies of {0}.'.format('R' + wanted[-4:]))
print(s)

if 'R' in s:
    print("\nBabayev'd\tbe\tproud\tof\tyou,\t\n\nlittle one.\n\a")


