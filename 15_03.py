#Leggere da un file (persone.txt) i nomi, cognomi e eta di un gruppo di persone. organizzarli in un dizionario 
#la cui chiave è il cognome e il cui valore è una t-upla contenente i tre valori letti.



pers=open("persone.txt","r")
testo=pers.readlines()
pers.close()
persona=[]
for i in testo:
    persona.append(i.strip())

for k in persona:
    persone=k.split(",")
    print("Nome:",persone[0],"Cognome:",persone[1],"Età:",persone[2])