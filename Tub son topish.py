import math
def TubSonQaytar(Son):
    num = 0
    i=1
    while (i<=Son):
        if (Son % i == 0):
            num=num+1
        i=i+1
        
    if(num==2):
        return str(Son)+" tub son"
    else:
        return str(Son)+" tub son emas"
        
SonKirit=int(input("Son kiriting: "))
print(TubSonQaytar(SonKirit))

def TubAjrat(son,bulinuvchi):
    num1 = 0
    while (son % bulinuvchi == 0):
        num1=num1+1
        son = son/bulinuvchi
    return str(num1)
SonKiriting=int(input("Son kiriting"))
Bulinuvchi=int(input("Bulinuvchini kiriting"))
print(SonKiriting," soni ",Bulinuvchi," ning ",TubAjrat(SonKiriting,Bulinuvchi)," darajasiga qoldiqsiz bo'linadi")

