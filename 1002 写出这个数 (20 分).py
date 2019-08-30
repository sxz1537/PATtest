n=input()
sum=0
for i in str(n):
    sum=sum+int(i)
d={'1':'yi','2':'er','3':'san','4':'si','5':'wu','6':'liu','7':'qi','8':'ba','9':'jiu','0':'ling'}
L=[]
for j in d.items():
  L.append(j)
for i in str(sum):
 for j in L:
  if i==j[0]:
    print j[1],
