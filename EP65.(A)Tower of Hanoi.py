def hanoi(n,a,b,c):
    # a => c
    if(n==0): # ถ้า n = 0 ให้จบการทำงาน
        return
    hanoi(n-1,a,c,b) # ย้าย a (ล,ก) -> b | c
    print(n )
    # hanoi(n-1,b,a,c)

hanoi(3,"A","B","C")