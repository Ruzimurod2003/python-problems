a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
i=0
if a>0 and b>0 and c>0:
    i=i+3
elif (a>0 and b>0 )or(b>0 and c>0)or(c>0 and a>0):
    i=i+2
elif (a>0 or b>0 or c>0):
    i=i+1
print("Bu sonlardan ",i," tasi musbat");
##def MusbatManfiy(son):
##    if (son>0):
##        return 1
##    elif (son<0):
##        return 0
##    else:
##        return "Mavjud emas"
##MusMan=MusbatManfiy(a)+MusbatManfiy(b)+MusbatManfiy(c)
##print("Bu sonlardan ",MusMan," tasi musbat");
