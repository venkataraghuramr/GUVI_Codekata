n = int(input())
lst = list(map(str, input().split(" ")))
count = 0
for i in range(n):
    if lst[i] == 'P':
        count += 1
x = (count / n) * 100
if x > 25:
    print('Not Blacklisted')
else:
    print('Blacklisted')
