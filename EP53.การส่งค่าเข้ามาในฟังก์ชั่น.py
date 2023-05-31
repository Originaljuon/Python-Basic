# การรับค่าเข้ามาที่ function

def myData(name,lname,C): # ตัวแปร name ตัวนี้เราเรียกว่า Parameter
						# ถ้ามีพารามิเตอร์ 2 ตัว ต้องมีการกำหนดค่าทั้ง 2 ตัวไม่งั้นจะ Error
	print("ชื่อ = ",name,"นามสกุล = ",lname,"อายุ = ",C)

myData("Jojo","Ruksiam",25) # Jojo ถูกเข้าไปเก็บใน Name แล้วแสดงผลออกมา
myData("Nut","ใจดี",50)
myData(5,10,34)
myData("Jam","สุดหล่อ",59)
# กรณีที่ไม่เอา , มาคั่นตอนแสดงผลต้องแปลงเลข 5 เป็นสตริงก่อน ตัวอย่าง print("Hello"+str(name)) ถ้าไม่แปลงค่ามันจะ Error
fname="Kong"
lname="Ruksiamza 555"
age=40
myData(fname,lname,age) # ดูเหมือนโปรแกรมจะกำหนดอัตโนมัติว่าเค้าของ fname มาแทนที่ค่าของ name ทำให้ถูกจัดวางแทน name ในการแสดงผล
