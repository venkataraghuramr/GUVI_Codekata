a = int(input())
n = list(map(int, input().split()))

x = max(n)
y = min(n)
count = 0
for i in range(a):
    if n[i] == max(n):
        count += 1
        break
    count += 1
count1 = 0
for i in range(a):
    if n[i] == min(n):
        count1 += 1
        break
    count1 += 1
print(count - count1)
