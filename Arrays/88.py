n = int(input())

bin_num = format(n,'b')
l1 = list(bin_num)
count = 0
for i in range(len(bin_num)):
    if l1[i] == '1':
        count = count+1       
print(count)
    
    