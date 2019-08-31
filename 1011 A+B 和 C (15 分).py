def isTrue(x,y,z):
    if x+y>z:
        return True
    return False

N=int(input())
for i in range(1,N+1):
    x,y,z=map(int,input().split())
    t=isTrue(x,y,z)
    if t:
        print ("Case #",end="")
        print (i,end="")
        print (': true')
    else:
        print ("Case #",end="")
        print (i,end="")
        print (': false')