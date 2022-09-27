slst = list(map(str, input().split(' ')))
l1 = []
for i in range(len(slst)):
    a = slst[i]
    a = a[::-1]
    l1.append(a)
x = " ".join(l1)
print(x)
