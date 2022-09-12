a=int(input("a="))
b=int(input("b="))
amal=input("+/-///*:")
if amal=="+":
    c=a+b
elif amal=="-":
    c=a-b 
elif amal=="/":
    c=a/b
elif amal=="*":
    c=a*b
else:
    c="xato"
print("Natija=", c)
