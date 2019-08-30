L=[]
n=input()
for i in range(n):
    L.append(raw_input())
for i in L:
    left=0
    mid=0
    right=0
    t=0
    p=0
    for j in i:
        if j=='A' and p==0 and t==0:
            left=left+1
            continue
        if j=='P':
            p=p+1
            continue
        if j == 'A' and p == 1 and t == 0:
            mid=mid+1
            continue
        if j=='T' and mid>=1:
            t=t+1
            continue
        if j=='A' and p==1 and t==1:
            right=right+1
            continue
        else:
            break
    if (p == 1 and t == 1 and left * mid == right):
        print "YES"
    else:
        print "NO"
        
        
    
