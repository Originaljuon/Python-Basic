# Union
fruitA={"กล้วย","มะยม","มะนาว"}
fruitB={"สตรอเบอร์รี่","กีวี่","มะม่วง"}
fruitA1={"กล้วย","มะยม","มะนาว"}
fruitB1={"สตรอเบอร์รี่","กีวี่","มะม่วง"}

allFruit=fruitA.union(fruitB) # เป็นการรวมข้อมูล 2 Set เข้าด้วยกัน สังเกตว่าพอรวมแล้วการเรียงลำดับข้อมูลที่แสดงผลเป็นแบบสุ่ม 
print(allFruit)

fruitA.update(fruitB) # เป็นการนำสมาชิกใน set หนึ่งเพิ่มเข้าไปใน set หนึ่ง ในกรณีนี้คือ fruitB เพิ่มเข้าไปยัง fruitA
print(fruitA)

fruitC=fruitA.copy() # เป็นการ copy ข้อมูลใน set หนึ่งสร้างขึ้นมาในอีก set หนึ่ง
print(fruitC)

fruitA.update(["แอปเปิ้ล","ทุเรียน"])
fruitB.update(["แอปเปิ้ล","ทุเรียน"])
fruitA1.update(["แอปเปิ้ล","ทุเรียน"])
fruitB1.update(["แอปเปิ้ล","ทุเรียน"])

fruitD=fruitA.difference(fruitB) 	# เป็นการบอกว่า 1.ถ้าข้อมูลไหนเหมือนกันให้เอาออก 2.ถ้าข้อมูลใน fruitB มี แต่ fruitA ไม่มีก็นำเอาออกเหมือนกัน
print(fruitD)						# ที่เหลือที่ไม่ถูกนำออกจะเก็บเข้าไปใน fruitD

fruitE=fruitA.intersection(fruitB) #เป็นการถามว่าข้อมูลที่เหมือนกันในทั้งสองเซตให้มาอยู่ใน fruitE แล้วแสดงผล
print(fruitE)

print("before =>",fruitA)
fruitA.difference_update(fruitB) #เป็นการใช้ difference เหมือนกัน แต่กรณีจะเก็บค่าลงไปใน fruitA เลยแบบอัตโนมัติ โดยไม่จำเป็นต้องสร้างตัวแปรใหม่
print("after =>",fruitA)

print(fruitA1)
fruitA1.intersection_update(fruitB1) 	# นำแค่ข้อมูลเหมือนกันแสดงผล
print(fruitA1)							# ถ้าไม่มีข้อมูลที่เหมือนกันเลยในแต่ละ set จะแสดงเป็นเซตเปล่า set()

#subset
fish={"ปลาดุก","ปลาหมอ","ปลาวาฬ","ปลาโลมา","ปลาฉลาม","ปลาตะเพียน"}

x={"ปลาดุก","ปลาฉลาม"}
xx={"ปลาวาฬ","ปลาฉลาม"}
y={"ปลาดุก","ปลาซิว"} # มีสมาชิกที่เหมือนกับ set fish ตัวเดียว ไม่เหมือนทั้งหมดอย่าง Set x


print(x.issubset(fish)) # เป็นการถามว่า x เป็น subset ของ fish หรือเปล่า? # เป็น boolean True or False
print(xx.issubset(fish)) # xx เป็น subset ของ fish หรือเปล่า?
print(y.issubset(fish)) # คำตอบคือ false แปลว่า y ไม่เป็น subset ของ fish

print(fish.issuperset(x)) # เป็นการถามกลับกันว่า fish เป็น supperset ของ x หรือ y หรือเปล่า ?
print(fish.issuperset(xx))
print(fish.issuperset(y))

# min , max เช็คค่าต่ำสุดกับสูงสุดใน set ไม่มีอะไรซับซ้อน!
number={3,4,5,100,80,900,1000,500,300,-100,-8,-150}

print(min(number))
print(max(number))