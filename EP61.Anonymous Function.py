# Anonymous Function == Lambda Function # คือ ฟังก์ชั่นที่เราสร้างขึ้นมาแล้ว "ไม่ต้องระบุชื่อ"

"""
lamda arguments : expression # โครงสร้างของ Lamda Function

"""

x=lambda name:name # return ไม่สารถใช้ได้กับ lamda เพราะปกติ lamda จะ return ในตัวของมันอยู่แล้ว
# วิธีเรียกใช้ lamda คือ การสร้างตัวแปรรับค่าเข้าไปในบรรทัดข้างบนคือ ตัวแปร "x"
sum=lambda x,y : x+y
multiply=lambda a,b : a*b

print(x("Kongruksiam"))
print(sum(5,10))
print(multiply(5,10))

result=multiply(5,10) # ตัวอย่างจำลองการสร้างตัวแปรเชื่อมกันข้อมูลจาก "multiply ไปสู่ result"
print(result)

def myPower(x):
    return "เลขยกกำลังของ", x, x*x

def myPowers(x):
    #  x = ตัวเลข
    #  a = เลขชี้กำลัง
    return lambda a : x**a

y=myPower(5)

z=myPowers(5) 
result=z(4)
"""
ตัวอย่างด้านบน คือ วิธีการเรียกใช้ฟังก์ชั่นปกติกับฟังก์ชั่น lambda ที่อยู่ข้างใน
ข้อสังเกต คือ "result=z(2)" บรรทัดนี้จะสลับไปอยู่ข้างบนบรรทัดที่เขียนว่า "z=myPowers(5)" ไม่ได้
ต้องพยายามเข้าใจหลักการทำงานของมัน
1. z=myPower(5) คือ การส่งเลข 5 เข้าไปในส่วนของ x 
   จาก lambda a " x**a กลายเป็น lamba a : 5**a จะเห็นว่าค่า a ยังไม่มีการระบุตัวเลขทำให้ยังหาค่า multiply ไม่ได้
2. result=z(2) คือ การบอกว่า ค่า a ของ lambda มีค่า = 2 ทำให้
   a : 5**a กลายเป็น 2 : 5**2 ทำให้สามารถหาค่าผลลัพธ์ได้แล้ว
3. ทำไมต้องมี a สองตำแหน่งเพราะ a ตำแหน่งแรกมีหน้าที่รับค่าเท่านั้น a ตำแหน่งที่สองมีหน้าที่มาหาค่าผลลัพธ์
"""

print(y)
print(result)