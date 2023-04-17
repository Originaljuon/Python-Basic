# 1+2+3+4+5
i=1
summation = 0
average = 0 # ผลรวม / จำนวนรอบ

while i<=10:
    summation+=i
    print("รอบที่ = ", i ,"ค่า sum = ",summation)
    i=i+1
    
average=summation/10

print("ผลรวมการบวกเลข = ",summation)
print("ค่าเฉลี่ย = ", average)