intlst = []
strlst = []
for i in range(10):
    x = int(input("Insert an integer: "))
    intlst.append(x)
for i in range(10):
    y = str(input("Insert a string: "))
    strlst.append(y)

print(intlst)
print(strlst)

import random

for i in range(len(intlst)):
    intlst[i] = random.randint(0,100)

print(intlst)