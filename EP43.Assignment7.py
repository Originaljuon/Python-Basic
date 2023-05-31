# จับคู่คำทักทาย / บุคคล

greeting=["สวัสดี" , "Hello" , "Good Bye"]
people=["ก้อง","แก้ม","โจ้"]
result=[ ]
#แบบปกติ
# for x in greeting:
#     for y in people:
#         result.append(x+y)

# print(result)

#ลดรูป
result=[x+y for x in greeting for y in people]
print(result)
