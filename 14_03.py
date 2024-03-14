fin= open("alice.txt","r")
linee=fin.read()
fin.close()
l1=[]
car=len(linee)
car2=0
car3=0
for i in linee:
    if i!=" ":
        car2+=1
for i in linee:
    if i.isalnum() or i.isalpha():
        car3+=1
print(car)
print(car2)
print(car3)

"""lista=[]

for l in linee:
    l=l.split(" ")
    lista.extend(l)
for k in range(0,(len(lista)-1)):
    print(lista[k])"""


"""def nonvuota(ls):
    l1=[]
    for i in ls:
        if len(i.strip())!=0:
            l1.append(i)
    return l1

ls=["uno","","due","tre","","",""," ","  ","fine"]
print(nonvuota(ls))"""