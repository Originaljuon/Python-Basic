for i in range(0,10,3): # (start,stop,step)
    print("รอบที่ = ",i,"Kiattikhoon")
"""
1.ค่าตำแหน่งเริ่มต้นของ Loop นี้ คือ 0
2.ตัวเลขสุดท้ายที่เราระบุไว้ จะไม่เกิดรอบนั้นขึ้น
    ตัวอย่าง ถ้าระบุไว้ว่า
        for i in range(4) ผลลัพธ์ที่ได้จะเป็นดังนี้
            รอบที่ 0 = แสดงผล
            รอบที่ 1 = แสดงผล
            รอบที่ 2 = แสดงผล
            รอบที่ 3 = แสดงผล
            รอบที่ 4 = ไม่แสดงผล
3.เราสามารถกำหนด "จุดเริ่มต้น" ได้ 
    ตัวอย่าง ถ้าเราระบุว่า 
        for i in range(1,4) ผลลัพธ์ที่ได้จะเป็นดังนี้
            รอบที่ 0 = ไม่แสดงผล # เลข 1 เหมือนเป็นการบอกว่าตำแหน่งที่ 1 ไม่นับ ซึ่งตำแหน่งที่ 1 เริ่มต้นด้วย 0
            รอบที่ 1 = แสดงผล 
            รอบที่ 2 = แสดงผล 
            รอบที่ 3 = แสดงผล 
            รอบที่ 4 = ไม่แสดงผล
4.ตัวเลขตำแหน่งที่ 3 เป็นตัวเลขที่บอกว่าให้นับทีละเท่าไร เหมือนการหาร ,ค่า default อยู่ที่ 1
    ตัวอย่าง
        for i in range(1,10,3) # แปลก็คือให้เริ่มนับตั้งแต่ตำแหน่งที่ 2 จนถึง ตำแหน่งที่ 9 โดยให้นับทีละ 3
        ผลลัพธ์ที่ได้
            รอบที่ 0  = ไม่แสดงผล # เพราะ จุดเริ่มต้นมีการระบุเลขที่ 1 หมายถึง ค่าในตำแหน่งที่ 0 ไม่นับ
            รอบที่ 1  = แสดงผล # เป็นจุดเริ่มต้นการนับค่าและแสดงผล
            รอบที่ 2  = ไม่แสดงผล # นับ 1
            รอบที่ 3  = ไม่แสดงผล # นับ 2
            รอบที่ 4  = แสดงผล # นับ 3 แสดงผล
            รอบที่ 5  = ไม่แสดงผล # นับ 1
            รอบที่ 6  = ไม่แสดงผล # นับ 2
            รอบที่ 7  = แสดงผล # นับ 3 แสงผล
            รอบที่ 8  = ไม่แสดงผล # นับ 1
            รอบที่ 9  = ไม่แสดงผล # นับ 2
            รอบที่ 10 = ไม่แสดงผล # นับ 3 ปกติต้องแสงผลแต่เนื่องจาก พารามิเตอร์ตำแหน่งที่ 2 ระบุไว้ที่เลข 10 หมายถึง ให้หยุดที่ตำแหน่งที่ 9 จึงไม่มีการแสดงผลอีก

5. ถ้าเราอยากระบุให้ start = 0 stop = 7 step = 3
   เราจะเขียนแบบนี้ for i in range(7,3) แบบนี้ไม่ได้ ต้องมีระบุค่า start ไปด้วย
   คือ for i in range(0,7,3) แบบนี้ค่าถึงจะทำงานแบบที่เราต้องการ
"""
summation=0

for i in range(0,7,2): # summation
    summation+=i
    print("รอบที่ = ",i,"sum = ",summation)

print("ผลรวม = ", summation)

"""
1.ค่า summation เป็นผลรวมที่มีการนำผลรวมเก่ามาบวกได้ต่อกันไปเรื่อยๆ
2.ถ้ามีการเพิ่มค่า step ไปด้วย ค่า summation จะนับโดยอ้างอิงกับ step ไม่นับผลบวกสะสมทุกๆรอบ(รอบที่ไม่ลง step ก็ไม่นับ)
"""

# สร้าง loop นับถอยหลัง
for i in range(10,0,-1):
    # การนับจาก 10,0 กับการนับจาก 0,10 "ไม่เหมือนกัน" เป็นข้อสังเกตเมื่อไรที่เราคิดว่าเหมือนกันจะทำให้เรางงได้
    print("รอบที่ = ",i)
# เป็นการบอกว่าให้เริ่มนับในตำแหน่งที่ 10 ลดลงมาทีละ 1 ไปถึงตำแหน่งที่ 1 (ก่อนที่ตำแหน่งที่ 0 ตามที่ระบุไว้)
# อย่าลืม (start,stop,step)

# Loop ซ้อน Loop
i=1
while i<=3 :
    j=1 # ตัวนับ
    while j<=5 :
        print("รอบที่ = ",i," ตำแหน่งที่ = ", j)
        j+=1 # j = j + 1 , ค่าเริ่มต้นของ j ในครั้งแรก คือ 1 ดังนั้น 1 = 1 + 1 j = 2 แล้ววนไปรอบต่อไปจนกว่าเงื่อนไขจะเป็นเท็จ
    i+=1
    # ที่น่าสนใจคือ ถ้าตามตัวอย่างข้างบนเอา line 66 and line 67 ออก Loop ก็ทำงานต่อไปเรื่อยๆ"ไม่มีที่สิ้นสุด"

for i in range(1,4):
    print("รอบที่ = ", i)
    for j in range(1,6):
        print("ตำแหน่งที่ = ", j)

for i in range(1,4):
    for j in range(1,6):
        print("รอบที่ = ",i,"ตำแหน่งที่ = ", j) # ลองประยุกต์เขียนอีกรูปแบบหนึ่ง

# Assignment about Loop
# แม่สูตรคูณ (Multiplication Table)
for i in range(2,4):
    print("แม่ = ",i)
    for j in range(1,13):
        print(i,"x",j,"=",i*j) # ในคลิป Kongruksiam ใส่วงเล็บตรง i*j ความเห็นส่วนตัวคิดว่าไม่ต้องใส่ก็ได้เกินความจำเป็น

start=int(input("แม่สูตรคูณ =")) # สามารถป้อนค่าได้ด้วยคำสั่ง input แต่อย่าลืมแปลงค่าเป็น int ก่อน

for x in range(start,start+1):
    print("แม่ =",x)
    for y in range(1,13):
        print(x,"x",y,"=",x*y) # ประยุกต์จากที่ Kongruksiam นำเสนอไว้