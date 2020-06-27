s = input("Enter your string: ")
summ = 0
L1 = []

for i in range(len(s)):
    print("ASCII value of " + s[i] + " is " , ord(s[i]), end = "\n")
    summ += int(ord(s[i]))
    L1.append(ord(s[i]))

print(summ, end = "\n")

L2 = [ord(c) for c in s]
L3 = list(map(ord, s))

print(L1, L2, L3)


