import json


#Per leggere un file json 
filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()
# !!!! SONO TUTTE OPERAZIONI SU LISTE !!!!
# 1) contare quanti calciatori hanno giocato per l'Italia
# 2) contare quanti calciatori hanno giocato per il Brasile
# 3) contare quanti calciatori hanno giocato per l'Argentina
# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
# 9) Trovare quale squadra di calcio ha fornito più calciatori per la coppa del mondo
#    Organizzare per nazione. Cioè quale squadra italiana ha fornito più calciatori per la coppa del mondo e quanti, quale squadra francese, ...

"""
#Esempio:
quantiCalciatori = dict()
for v in worldcup:
    # se v.Team è già presente, sommo 1, altrimenti metto a 1
    if v["Team"] in quantiCalciatori.keys():
        quantiCalciatori[v["Team"]]=quantiCalciatori[v["Team"]]+1
    else:
        quantiCalciatori[v["Team"]]=1

print(quantiCalciatori)
"""

# 1) contare quanti calciatori hanno giocato per l'Italia
ita=[]
for i in worldcup:
    if i["Team"] =="Italy" or i["Team"] =="ITA":
        ita.append(i["FullName"])
ita=set(ita)
print("Giocatori che hanno giocato per l'Italia:",len(ita))

# 2) contare quanti calciatori hanno giocato per il Brasile
bra=[]
for b in worldcup:
    if b["Team"]=="Brazil" or b["Team"]=="BRA":
        bra.append(b["FullName"])
bra=set(bra)
print("Giocatori che hanno giocato per il Brasile:",len(bra))

# 3) contare quanti calciatori hanno giocato per l'Argentina
arg=[]
for a in worldcup:
    if a["Team"]=="Argentina" or a["Team"]=="ARG":
        arg.append(a["FullName"])
arg=set(arg)
print("Giocatori che hanno giocato per l'Argentina:",len(arg))

# 4) Indicare quali calciatori hanno giocato sia per il Brasile, sia per l'Italia
print("Calciatori che hanno giocato sia per l'Italia sia per il Brasile:",ita.intersection(bra))

# 5) Indicare quali calciatori hanno giocato sia per l'Argentina, sia per l'Italia
print("Calciatori che hanno giocato sia per l'Italia sia per l'Argentina:",ita.intersection(arg))

# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa del mondo
i=0
max=[0,0,0]
eta=[]
count=0
for k in worldcup:
    if k["DateOfBirth"]!="":
       eta= k["DateOfBirth"].split("-")
       if int(eta[0])> int(max[0]):
           max=eta
           count=i
    i+=1
for v in worldcup:
    eta= v["DateOfBirth"].split("-")
    if eta==max:
        print("Il giocatore più anziano è:",worldcup[count]["FullName"])

# 7) Trovare qual'è il calciatore più anziano che ha partecipato alla coppa del mondo
i=0
min=[2024,3,16]
eta=[]
for k in worldcup:
    if k["DateOfBirth"]!="":
       eta= k["DateOfBirth"].split("-")
       if int(eta[0])< int(min[0]):
           min=eta
           count=i
    i+=1
for v in worldcup:
    eta= v["DateOfBirth"].split("-")
    if eta==min:
        print("Il giocatore più giovane è:",worldcup[count]["FullName"])

# 8) Trovare quale calciatore ha partecipato a più edizioni della coppa del mondo
volte = dict()

for v in worldcup:
    if v["Team"] in volte.keys():
        volte[v["FullName"]]=volte[v["FullName"]]+1
    else:
        volte[v["FullName"]]=1
for m in worldcup:
    if volte[m["FullName"]]>max:
        max=m
print(max)