import math
FibXad=int(input("Fibonachini hadini kirgizing: "))
def fibonachi(son):
    if (son==0 or son==1):
        return 1
    else:
        return (fibonachi(son-1)+fibonachi(son-2))
i=0
while i<=FibXad:
    print("Fibonachining ",i," hadi ",fibonachi(i)," ga teng")
    i=i+1
    
input()
