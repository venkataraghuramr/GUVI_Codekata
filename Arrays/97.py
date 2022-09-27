n = int(input())
l1 = list(map(int,input().split(" ")))
l2 = list(map(int,input().split(" ")))

if l1 == l2[::-1]:
    print('yes')
elif l2 == l1[::-1]:
    print('yes')
else:
    print('no')

