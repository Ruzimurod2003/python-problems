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
