r1=int(input("Inserisci valore raggio 1->"))
r2=int(input("Inserisci valore raggio 2->"))
r3=int(input("Inserisci valore raggio 3->"))
h=int(input("Inserisci valore altezza->"))
π=3.1415
s1=π*(r1**2)
s2=π*(r2**2)
s3=π*(r3**2)
v=1/6*h*(s1+4*s2+s3)
l=v/1000
print("La botte puo contenere ",l,"litri")