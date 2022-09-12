##i=int(input('Son kiriting: '))
##suz=""
##for k in range(0,i):
##    if (k % 2==0):
##        suz=suz+"  "+str(k)
##print(suz)      
##(n*(n-1)...(n-k+1))/(1*2*3...k)
k=int(input('k ni kiriting: '))
n=int(input('n ni kiriting: '))
u=1
fact=1
while u<=k:
    fact=fact*u
    u=u+1
m=1
for  t  in range((n-k+1),n):
    m=m*t
print(str(m))
