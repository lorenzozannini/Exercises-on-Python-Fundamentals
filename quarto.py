import random

#sapendo che la funzione random.randint(start, end)
#genera un numero intero compreso tra start e end, end compreso,
#costruire una lista di numeri casuali lunga 100 e
#stampare la somma di tutti i suoi numeri
    
l=[]
somma=0
for i in range(100):
    r=random.randint(1,10)
    l.append(r)
    somma=somma+r
print(l)
print(somma)

#Costruire due liste, la prima che contiene i numeri pari fino a 1000
#la seconda che contiene i numeri dispari fino a 1000
#a partire dalle prime due liste,
#costruire una terza lista che contiene prima tutti i pari e poi tutti i dispari
l1=[]
l2=[]
l3=l1

for i in range(0,1001,2):
    l1.append(i)

for k in range(1,1001,2):
    l2.append(k)

print(l1)
print(l2)
for i in l2:
    l3.append(i)
print(l3)
