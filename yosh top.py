import math
sonkiritish="Uchburchak tomonlarini kiriting:  "
a=int(input(sonkiritish))
b=int(input(sonkiritish))
c=int(input(sonkiritish))
maxson=max(a,b,c)
minson=min(a,b,c)
if a>b and a<c:
    srson=a
elif b>c and b<a:
    srson=b
else:
    srson=c

if (maxson<srson+minson) :
    print("Uchburchak mavjud emas")
elif (math.pow(srson,2)+math.pow(minson,2))>math.pow(maxson,2):
    print("O'tkir burchakli uchburchak")
elif (math.pow(srson,2)+math.pow(minson,2))==math.pow(maxson,2):
    print("To'g'ri burchakli uchburchak")
elif (math.pow(srson,2)+math.pow(minson,2))<math.pow(maxson,2):
    print("O'tmas burchakli uchburchak")

input()
    
