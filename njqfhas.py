#Leggere da un file (persone.txt) i nomi, cognomi e eta di un gruppo di persone. organizzarli in un dizionario 
#la cui chiave è il cognome e il cui valore è una t-upla contenente i tre valori letti.



pers=open("persone.txt","r")
testo=pers.readlines()
pers.close()
persone=[]
persona=[]
l=[]
for i in testo:
    persona.append(i.strip())

for k in range(0,len(persona)):
    l.extend(persona[k].split(","))
    persone.append(l)
    l=[]
print(persone)