son1=int(print("Birinchi son:"))
m1=son1
son2=int(input("Ikkinchi son:"))
m2=son2
while (son1 !=son2):
    if (son1>son2):
        son1=son1-son2
    if (son1<son2):
        son2=son2-son1
print("EKUB(",m1," , ",m2,")=",son1)
print("EKUK(",m1," , ",m2,")=",int(m1*m2/son1))

input()