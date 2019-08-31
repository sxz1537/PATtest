M,N=(map(int,input().split()))
count=0 #素数的个数
showNUM=0 #已经输出素数的个数，便于换行
for i in range(2,10001):  
    for j in range(2,i):
        if (i % j) == 0:
            break
    else:
        count=count+1
        if count>N:
            break
        if count>=M:
            showNUM=showNUM+1
            if showNUM%10==0 or count==N:               
                print (i)
            else:
                print (i,end=" ")
            