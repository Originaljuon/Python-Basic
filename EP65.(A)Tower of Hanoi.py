def hanoi(n,a,b,c):
    # a => c
    if(n==0): # ถ้า n = 0 ให้จบการทำงาน
        return
    hanoi(n-1,a,c,b) # ย้าย a (ล,ก) -> b | c
    print("จานที่ = ",n ,"จาก = ",a,"ไป = ",c)
    print("จานที่ = ",n ,"จาก = ",a," ไป = ",c)

hanoi(4,"A","B","C")