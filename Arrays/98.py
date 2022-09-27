string, k = map(str, input().split(" "))
k = int(k)
y = k
str_lst = list(string)
l2 = []
for i in range(len(str_lst)):
    if k <= len(str_lst):
        a = str_lst[k - 1]
        l2.append(a)
    k += y

x = " ".join(l2)
print(x)
