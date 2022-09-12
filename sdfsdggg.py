def ekub(a,b):
    while a != 0 and b != 0:
        if a>b:
            a %=b
        else:
            b %=a
            ekub_q=a+b
    return ekub_q
a=int(input("a="))
b=int(input("b="))
print(ekub(a, b))
