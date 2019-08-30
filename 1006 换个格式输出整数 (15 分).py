l=[]
s=''
num=input()
x=num/100
y=(num-100*x)/10
z=num%10+1
for i in range(x):
    l.append('B')
for i in range(y):
    l.append('S')
for i in range(1,z):
    l.append(i)
for i in l:
    s=s+str(i)
print s