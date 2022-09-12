Son=int(input("Son kiriting: "))
i=1
buluvchi=""
while i<=Son:
    if ((Son % i)==0):
        if (i % 2 ==0):
            buluvchi=buluvchi+" "+str(i)
    i=i+1
print(buluvchi)
