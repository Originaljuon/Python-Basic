# Global Variable / Local Variable

def displayNumber():
	# statenebt
	x=10 # ตัวนี้คือ Local Variable
	a=100
	print("Hello = ",x,a," ใน ") # เป็นการกำหนดว่าถ้าเราเรียกใช้ function displayNumber จะต้องมีข้อความว่า Hello = 10( 10 คือค่าตัวแปรของ x )



# โปรแกรมหลัก
x=20 # ตัวนี้คือ Global Variable
a=200
print("Hello = ",a," นอก ")
displayNumber()