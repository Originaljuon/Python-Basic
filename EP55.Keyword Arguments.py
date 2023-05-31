# Keyword Arguments

def displayData(fname,lname,city):
    print("ชื่อ = ",fname)
    print("นามสกุล = ",lname)
    print("จังหวัด = ",city)

displayData("kong","ruksiam","bangkok") # ต้องเขียนเรียงลำดับตามค่าที่เราตั้งไว้ในฟังก์ชั่น


# ถ้าเราอยากป้อนข้อมูลโดยไม่ต้องเรียงลำดับฟังก์ชั่นต้องมีการระบุ keyword argument ลงไปด้วย ตัวอย่างด้านล่าง

displayData(city="ระยอง",lname="ใจดี",fname="นัท")

# Default Parameter
def displayDatas(fname,lname,city="กรุงเทพ"): # city = "กรุงเทพ" เป็นการกำหนดค่า Default Parameter
    print("ชื่อ = ",fname)
    print("นามสกุล = ",lname)
    print("จังหวัด = ",city)

displayDatas(city="ระยอง",lname="ใจดี",fname="นัท")
displayDatas(fname="โจโจ้",lname="หล่อมาก") # ปกติเราต้องป้อนข้อมูลให้ครบ 3 ที่ ให้สอดคล้องกับ Parameter ไม่งั้นจะ error แต่ถ้ามีการกำหนดค่า Default ก็จะ่ไม่จำเป็นป้อนข้อมูล 3 ที่ ก็ได้

# List Parameter
def displayFruit(item):
	for i in range(len(item)):
		print("ผลไม้ชิ้นที่",i+1 ," = " , item[i])
def displayVet(item):
	for i in range(len(item)):
		print("ผักชนิดที่",i+1 ," = " , item[i])

fruit=["มะม่วง","มะละกอ","ฝรั่ง","มะนาว"]
vet=('ชะอม','ผักกาด','คะน้า')
displayFruit(fruit)
displayVet(vet)