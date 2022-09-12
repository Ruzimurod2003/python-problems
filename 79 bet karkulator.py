a=int(input("a="))
b=int(input("b="))
amal=input("amallardan birini toping:+/-/*//:")
if amal=="+":
    c=a+b
elif amal=="-":
    c=a-b
elif amal=="/":
    c=a/b
elif amal=="*":
    c=a*b
else:
    c="Xato"
print("natija: c=",c)
