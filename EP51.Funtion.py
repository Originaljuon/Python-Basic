a,b,c,d=10,23,40,50

if a%2 == 0: # ถามว่าหารเลข 2 ลงตัวหรือไม่ ?
    print("เลขคู่")
else :
    print("เลขคี่")
if b%2 == 0:
    print("เลขคู่")
else :
    print("เลขคี่")
if c%2 == 0:
    print("เลขคู่")
else :
    print("เลขคี่") 
if d%2 == 0:
    print("เลขคู่")
else :
    print("เลขคี่") # จะสังเกตได้ว่ามีการใช้คำสั่งซ้ำกันหลายที่
				  # ลองสร้างฟังก์ชั่นของตัวนี้ดู

# การสร้าง function / เรียก function
# def ชื่อฟังก์ชั่น () :
#	  statement

def sayHi():
    print("Hello Function")
    
def sayThailand():
    print("สวัสดี")

def sayEngland():
    print("Hello / Hi")
def add():
    x=3+1
    print(x)


# โปรแกรมหลัก
add()
sayThailand() # วิธีเรียกใช้ฟังก์ชั่น 1.เขียนชื่อฟังก์ชั่น 2.ใส่วงเล็บ จบ
sayEngland()
sayEngland()

for i in range(4): # ทำงานร่วมกับ loop
	add()