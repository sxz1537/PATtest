str1=input()
str2=input()
str3=input()
str4=input()
L1=[]
L2=[]
d1={'A':'MON ','B':'TUE','C':'WED','D':'THU','E':'FRI','F':'SAT','G':'SUN'}
d2={ '0':'00','1':'01','2':'02','3':'03','4':'04','5':'05','6':'06',
'7':'07','8':'08','9':'09','A':'10','B':'11','C':'12','D':'13',
 'E':'14','F':'15','G':'16','H':'17','I':'18','J':'19','K':'20',  
 'L':'21','M':'22','N':'23'}

for i in d1.keys():
    L1.append(i)
for i in d2.keys():
    L2.append(i)
def getWeek():
    global str1
    global str2
    for i in range(len(str1)):
        if str1[i]==str2[i]:
            if str1[i] in L1:
                print(d1[str1[i]],end=" ")
                str1=str1[i+1:]
                str2=str2[i+1:]
                return
def getHour():
    for i in range(len(str2)):
        if str1[i]==str2[i]:
            if str1[i] in L2:
                print(d2[str1[i]],end=":")
                return
def getMinu():
    for i in range(len(str3)): 
        if str3[i]==str4[i] and str3[i].isalpha():
            if i<10:
                tstr=str(i)
                return ('0'+tstr)
            return i          
getWeek()           
getHour()
print (getMinu())