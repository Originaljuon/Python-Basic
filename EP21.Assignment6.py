# โปรแกรมคำนวณค่า BMI (ดัชนี้มวลกาย) 2.0
# BMI = น้ำหนัก(kg) / ส่วนสูง * ส่วนสูง (m)
# input / convert to integer
weight=int(input("ป้อนน้ำหนักของคุณ (kg):"))
high=int(input("ป้อนส่วนสูงของคุณ (cm) :"))/100
bmi = weight/(high**2)

result="ไม่ทราบค่าที่ชัดเจน"
if bmi>=0 and bmi<18.4:
    result="ผอม"
elif bmi>=18.5 and bmi <=22.9:
    result="สมส่วน"
elif bmi>=23.0 and bmi <=24.9:
    result="น้ำหนักเกิน"
elif bmi>=25.0 and bmi <=29.9:
    result="โรคอ้วน ระดับที่ 1"
elif bmi>=30:
    result="โรคอ้วนระดับอันตราย"
else :
    result="ไม่ทราบค่าที่ชัดเจน"


print("ค่า bmi = ", bmi ,"ทำนายว่า =",result)

'''
<18 ต่ำกว่าเกณฑ์
18.5 - 22.9 = สมส่วน
23.0 - 24.9 = น้ำหนักเกิน
25.0 - 29.9 = โรคอ้วน ระดับที่ 1
>30 = โรคอ้วนระดับอันตราย

'''