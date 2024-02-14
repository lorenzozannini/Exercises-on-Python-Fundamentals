from math import radians,asin, cos, sin, sqrt
c1=10.123
c2=30.456
risultato=sqrt((c1**2)+(c2**2))
print("ipotenusa=",risultato)

r=6371
ϕ1=radians(59.9)
λ1=radians(10.8)
ϕ2=radians(49.3)
λ2=radians(-123.1)
d=2*r*asin(sqrt(sin(1/2*(ϕ2-ϕ1))**2 + cos(ϕ1)*cos(ϕ2)*sin(1/2*(λ2-λ1))**2))
print(d)