a=1
while a<=9:
    b=1
    while(b<=9):
        print(f"{a}*{b}={a*b}",end="\t")
        b+=1
    a+=1
    print("\t")