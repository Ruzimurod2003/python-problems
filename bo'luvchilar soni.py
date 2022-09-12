Son=int(input("Son kiriting: "))
i=1
buluvchi=""
while i<=Son:
    if ((Son % i)==0):
        buluvchi=buluvchi+" "+str(i)
    i=i+1

i=1
buluvchiToq=""
while i<=Son:
    if ((Son % i)==0):
        if i % 2 == 1:
            buluvchiToq=buluvchiToq+" "+str(i)
    i=i+1

print(Son," ning bo'luvchilari: ",buluvchi)
print(Son," ning toq bo'luvchilari: ",buluvchiToq)
