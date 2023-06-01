# Recursive Function = ฟังก์ชั่นที่เรียกฟังก์ชั่นตัวเอง

def a():
	print("A")
	b() # มีการกำหนดให้ฟังก์ชั่น a เรียกใช้งานฟังก์ชั่น b เป็นลักษณะที่ฟังก์ชั่นเรียกใช้งานอีกฟังก์ชั่นหนึ่งยังไม่ใช่ฟังก์ชั่นที่เรียกใช้งานฟังก์ชั่นตัวเอง

def b():
	print("B")


"""

วิธีสร้าง Recursive Function
1. หาจุดวนซ้ำ
2. หาจุดออกจาก function (return)
3.ต้องมี parameter

"""
# ถ้าตั้งโจทย์ 1-5 โดยไม่ใช้ คำสั่ง loop
def c():
	i=1
	print(i)
	i+=1
	c()

# c()


def addNumber(number):
	if number==5:
		return # มีการกำหนดจุดวนซ้ำ
	print(number+1) # 0
	number+=1 #1
	addNumber(number)


addNumber(0)

def summation(number):
	if number==1:
		return int() # บอกว่าถ้า number มีค่าเท่ากับ 1 ให้กระโดดออกมา (จบโปรแกรม)
	else :
		return number+summation(number-1) # ค่า default number = 5 แต่พอมีการเรียกใช้ฟังก์ชั่นในที่นี้คือ summation ค่าในส่วนของ number จะลดลงไปเรื่อยๆจนพอมาถึง 1 ก็จะออกจะปิดโปรแกรม

x=summation(5) # 5+4+3+2+1
print(x) # พอเข้าบล๊อก if ที่ไม่มีการเรียกใช้ function อีกเลยจบการทำงาน