N=input()
temp=1
count=0
for i in range(2,N+1):  
    for j in range(2,i):
        if (i % j) == 0:
            break
    else:
        if i-temp==2:
            count=count+1
        temp=i
print count
