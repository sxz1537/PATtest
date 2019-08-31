#定义一个函数 用于将数组移位1
def Moveit(L): 
    templ=[]
    for i in range(len(L)):
        templ.append(L[i-1])
    return templ
#输入N,M
N,M = map(int,input().split())
l1=list(map(int,input().split()))
for i in range(M):
    l1=Moveit(l1)
k=1
for i in l1:
    if k!=len(l1):
        print (i,end=" ")
        k=k+1
    else:
        print (i)