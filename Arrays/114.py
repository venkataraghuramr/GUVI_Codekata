n, k = map(int, input().split(" "))
lst = list(map(int, input().split(" ")))
count = 0
for i in range(n):
    if lst[i] == k:
        count += 1
a = str(count)
if count <= 0:
    print('no')
else:
    print("yes" + " " + a)
