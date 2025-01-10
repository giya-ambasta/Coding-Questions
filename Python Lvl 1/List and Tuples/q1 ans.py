n = int(input())
a=input().split()
sma=[]
summ=0
for i in range(1,n+1,2):
    if a[i]>a[i-1]:
        sma.append(a[i-1])
    else:
        sma.append(a[i])
for i in sma:
    summ+=int(i)
print(summ)