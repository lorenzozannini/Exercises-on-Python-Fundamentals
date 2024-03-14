import random
"""def pari (a,b,c):
    if a%2==0:
        print(b+c)
    else:
        print(b-c)
a=10
b=20
c=30
pari(a,b,c)
print(pari)"""





"""def ColoreCasuale():
    colori=["rosso","giallo","verde","blu","arancio","ciano"]
    print(colori[random.randint(0,(len(colori)-1))])

ColoreCasuale()
ColoreCasuale()
ColoreCasuale()
ColoreCasuale()"""

"""def digit():
    lista=[]
    for i in range(0,10000):
        s=str(i)
        while len(s)<4:
            s="0"+s
        lista.append(s)
    return lista


print(digit())"""


def split(sd):
    numeri=[]
    for i in sd:
        numeri.append(int(i))
    return numeri
    
print(split(input("123")))