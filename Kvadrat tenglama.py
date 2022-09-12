
import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=b**2-4*a*c
if d<0:
    print("Javob yo'q")
elif d==0:
    x=(-b)/(2*a)
    print("Bitta yechim bor va u:",x)
else:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)

    print("Ikkita yechim bor ular ",x1," va ",x2," ga teng")

