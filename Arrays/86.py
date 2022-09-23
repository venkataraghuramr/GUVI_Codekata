n = int(input())
lst = list(map(int,input().split(" ")))
sum = 0
for i in range(n-1):
    a = lst[i]+lst[i+1]
    sum = sum+a
    
    
print(sum)
    