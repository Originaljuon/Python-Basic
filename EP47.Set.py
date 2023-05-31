# แบบปกติ
fruit={"มะม่วง","มะขาม","มะยม"} # ลำดับใน set นั้นไม่แน่นอนการแสดงผลจึงเป็นแบบสุ่มสลับไปมา

print(fruit)

lis="ปลาทู","ปลาตะเพียน"
#constructor
fish=set(["ปลาดุก","ปลาหมอ","ปลาดุก"]) # เป็นการแสดงว่าถ้ามีข้อมูลเหมือนกัน เวลา print set ข้อมูลก็จะออกมาแค่ชุดเดียวไม่ออกข้อมูลซ้ำสองชุด
fishes=set(lis) # เป็นการแปลงค่า lis เป็น set สังเกตว่าพอ print แล้วตัว lis ที่เแปลงค่าเป็น set แล้ว มีวงเล็บปีกกาครอบในการแสดงผลซึ่งเป็นลักษณะเด่นของ set
print(fish)
print(fishes)

fruits={"มะม่วง","มะขาม","มะยม",50,True}

print(fruits) #เป็นการแสดงว่าถ้าไม่ใช่ string เพียงอย่างเดียวแต่มี integer และ boolean เข้ามาอยู่ใน set นั้นทำได้มั๊ย คำตอบคือ ได้

# เพิ่มข้อมูลสมาชิก อ้างอิงตัวแปรเริ่มต้นคือ fruit ตำแหน่งที่ line 2
fruit.add("ทุเรียน")
fruit.add("สับปะรด")
fruit.add("999")
fruit.add(999) 	# มีข้อสังเกตว่าถ้าเป็น int ไม่จำเป็นต้องใส่ฟันหนูก็สามารถเพิ่มสมาชิกได้แต่ถ้าเป็น str ถ้าไม่ได้ใส่ฟันหนูจะเกิดการ error
				# ข้อสังเกตอีกอันหนึ่งคือ "999" และ 999 มองว่าเป็นข้อมูลต่างชนิดกันทำให้เวลา print แสดงผลออกมาจึงออกมาทั้งสองข้อมูล

lis=["ตะไคร้","โหระพา","ชะอม"]
fruit.update(lis)
# เป็นการเพิ่มสมาชิกหลายตัวในคราวเดียวโดยใช้ lis ในการช่วย
fruit.update(["ยี่หร่า","มะนาว","มะพร้าว"])
# เป็นการเพิ่มสมาชิกหลายตัวเหมือนกันแต่คราวนี้จบภายในบรรทัดเดียว คีย์เวิร์ดน่าจะอยู่ที่มีการใช้ใช้วงเล็บเหลี่ยมเป็นการสื่อบอกว่าข้อมุลแบบ lis แล้ว

print(fruit)

# แสดงผลข้อมูลเป็นรายตัวในสมาชิกของ set (Loop)
for item in fruit:
    print("ข้อมูล =>",item)

# แสดงจำนวนสมาชิกใน set
print(len(fruit)) # len คือ คำสั่งให้นับสมาชิกใน fruit ว่ามีกี่ตัว ?

if "มะเฟือง" in fruit: # ถามว่ามี "มะเฟือง" อยู่ใน fruit หรือเปล่า ?
    print("มี")
else :
    print("ไม่มี")
    
print("มะเฟือง" in fruit) # ถามเหมือนกันว่า "มะเฟือง" อยู่ใน fruit หรือเปล่า แต่จะแสดงผลเพียงแค่ว่า True or False
print("มะเฟือง" not in fruit) # ถามกลับกันว่า "มะเฟือง" ไม่ได้อยู่ใน fruit ใช่มั๊ย ถ้าไม่อยู่ คำตอบคือ True ถ้าอยู่ คำตอบคือ False

print("before =>",fruit)
fruit.remove("ทุเรียน") # ลบข้อมูลคำว่า "ทุเรียน" ออกจาก fruit
print("after =>",fruit)

fruit.discard("มะปราง") # "มะปราง" คือข้อมูลที่ไม่มีในสมาชิกของ fruit
# discard นี้ ใช้ลบสมาชิกใน set ได้เหมือนกัน แต่จะต่างกันที่ถ้าใช้ remove แล้วปรากฎว่าข้อมูลที่เราต้องการจะลบไม่มีใน set จะเกิดการ error แต่ถ้าใช้ discard 	กรณีแบบนี้จะไม่เกิดการ error
# งั้น discard ก็น่าจะดีกว่า remove
print(fruit)

fruit.add("ทุเรียนทอด") # เพิ่ม "ทุเรียนทอด" แทนที่ "ทุเรียน"
print(fruit)

fruit.clear() 	# เป็นการลบข้อมูลในสมาชิก fruit ออกทั้งหมด 
				# กรณีที่ใช้ del fruit อันนี้คือการลบตัวแปรในที่นี้คือตัวแปร fruit จะหายออกไปเลยเสมือนไม่มีตัวแปรนี้เกิดขึ้นมา
print(fruit)