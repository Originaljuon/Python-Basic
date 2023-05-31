# frozen set
fruit=frozenset(["มะม่วง","มะยม","มะนาว"])
# fruit.add("ทุเรียน") # ที่ต้องทำให้เป็น comment เพราะว่า จะเกิดการ error จาก frozen set และทำให้คำสั่ง for item in fruit ไม่สามารถทำงานต่อได้
# fruit.discard("มะยม") # เหตุผลเหมือนกับข้างบน
# frozen set ไม่สามารถ add or discard ได้
print(fruit)

for item in fruit:
    print("ข้อมูล=>",item)
