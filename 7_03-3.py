numero=""
i=0
while True:
    c = input("Digita 0-9,+-/=: ")
    if len(c)>0:
        c=c[0]
    if len(c)==0:
        continue
    if c==",":
        if i<1:
            i=i+1
            numero=numero+c
        else:
            continue
    else:
        if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",","]:
                print("Il numero è",numero)
                break
        else:
            numero=numero+c
    