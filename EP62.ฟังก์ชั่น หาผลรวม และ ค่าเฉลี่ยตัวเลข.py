# assignment

def summation(number):
    total,avg=0,0
    # มีการสร้างตัวแปร"ใน"ฟังก์ชั่นเพื่อเก็บข้อมูล
    for i in number : # for i in number ต่างจาก for i in range ที่จะเรียงตามลำดับ 1,2,3,4... หรือตาม step ที่กำหนดไว้ for i in number จะอ้างอิงจาก ค่า arguments ที่ส่งเข้ามาใน parameter
        total+=i 
        """
         total = total + i 
         1.รอบที่ 1 ค่า total เริ่มต้นอยู่ที่ 0 ค่า i ตำแหน่งที่ 1 เท่ากับ(กลับสมการ) 0 + 1 = 1 วนเก็บไปใน number
         2.รอบที่ 2 total = 1 ค่า i ตำแหน่งที่ 2 เท่ากับ 1 + 2 = 3 วนเก็บไปใน number
         3.รอบที่ 3 total = 3 ค่า i ตำแหน่งที่ 3 เท่ากับ 3 + 3 = 6 วนเก็บไปใน number
         4.เมื่อ Loop จนครบค่า arguments แล้ว จึงไปที่ฟังก์ชั่น return เพื่อคืนค่า ที่สะสมล่าสุดนั้นคือ 6 = total

        """
        avg=total/len(number)
        # total ในสมการของ line 17 นี้จะเป็น total สุดท้ายของการ Loop นั่นคือ 6 หารด้วย จำนวน parameter ที่ส่งเข้ามา นั่นคือ 3 เท่ากับ 6/3 = 2.0 เก็บไปยังตัวแปร avg
    return total,avg



x=[1,2,3]
y,z=summation(x)
print(y)
print(z)
