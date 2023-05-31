# tuple => string
character=('k','o','n','g')
name="".join(character) # แปลง tuple ให้กลายเป็น string 
						# funtion join เป็น funtion ที่อยู่ใน string เหมือนกับว่ามีสะพานข้ามจาก tuple กลายเป็น string แล้ว
print(name)

# reverse tuple
x=(100,20,30,15,10,5,500)
y=reversed(x) # ต้องมีการสร้างตัวแปรมาเก็บค่า reversed(x) อันนี้ด้วยจะเขียนแค่ reversed(x) แค่นี้ไม่ได้
print(tuple(y)) # ตามคำอธิบาย ตัวแปร y ยังเป็นแค่ object จะเขียนแค่ print(y) ไม่ได้ต้องเปลี่ยน ตัวแปร y เป็น tuple ก่อน

# reverse tuple อีกแนวทางหนึ่งได้ผลลัพธ์เหมือนกัน
a=(100,20,30,15,10,5,500)
b=tuple(reversed(a))
print(b)
# ตำแหน่งของ tuple แตกต่างกัน มีข้อดีข้อเสียแตกต่างคงต้องพิจารณาแล้วแต่สถานการณ์ไป

# string to tuple
c="kongruksiam"
d=tuple(reversed(c))
print(d)
# การ reverse string ไม่มีอะไรซับซ้อน