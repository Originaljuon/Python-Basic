# โปรแกรมคำนวณค่า BMI (ดัชนี้มวลกาย)
# BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง (m)

weight=int(input("ป้อนน้ำหนักของคุณ (kg):"))
high=int(input("ป้อนส่วนสูงของคุณ (cm) :"))

#process
#cm => m
high=high/100
#calculate bmi
bmi=weight/(high*high)


#output
print("BMI = ",bmi)