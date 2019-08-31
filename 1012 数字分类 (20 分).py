def getA1(L):
    result=0
    isHave=False
    for i in L:
        if i%5==0 and i%2==0:
            isHave=True
            result=result+i
    if isHave==True:   
        return result
    return "N"
def getA2(L):
    result=0
    isHave=False
    flag=1
    for i in L:
        if i%5==1:
            isHave=True
            if flag==1:
                result=result+i
                flag=0
            else:
                result=result-i
                flag=1
    if isHave==True:   
        return result
    return "N"
def getA3(L):
    isHave=False
    result=0
    for i in L:
        if i%5==2:
            isHave=True
            result=result+1
    if isHave==True:   
        return result
    return "N"
def getA4(L): 
    isHave=False
    sum=0
    count=0
    for i in L:
        if i%5==3:
            isHave=True
            sum=sum+i
            count=count+1
    if count<2:
        result=sum
    else:
        result=round((sum/count),1)
    if isHave==True:   
        return result
    return "N"
def getA5(L): 
    isHave=False
    result=0
    for i in L:
        if i%5==4:
            isHave=True
            if i>result:
                result=i
    if isHave==True:   
        return result
    return "N" 
L=list(map(int,input().split()))
N=L[0]
L.pop(0)
print (getA1(L),end=" ")
print (getA2(L),end=" ")
print (getA3(L),end=" ")
print (getA4(L),end=" ")
print (getA5(L))
