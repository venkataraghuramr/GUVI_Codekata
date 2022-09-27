n, k = map(int, input().split(" "))
l1 = list(str(n))
l2 = []
for i in range(len(l1)):
    if l1[i].isdigit() == True:
        a = int(l1[i])
        l2.append(a)
count = 0
for i in range(len(l2)):
    if l2[i] == k:
        count += 1
if count == 0:
    print(-1)
else:
    print(count)
