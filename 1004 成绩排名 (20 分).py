L=[]
l=()
maxl=[0,0,0]
minl=[0,0,100]
n=input()
for i in range(n):
    str=raw_input()
    l = str.split()
    L.append(l)
for i in L:
    if int(i[2])>int(maxl[2]):
        maxl=i
for i in L:
    if int(i[2])<int(minl[2]):
        minl=i
print maxl[0],maxl[1]
print minl[0],minl[1]