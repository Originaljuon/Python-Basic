# Module จัดการวันและเวลา
# Module Date / Time
# "%x"(small x) = การย่อรูปแบบวันที่ให้กลายเป็น => m/d/y
# "%X"(Capital X) = แสดงในเรื่อง "เวลา" => h:m:s
# "%c" => วัน เดือน วันที่ ชั่วโมง:นาที:วินาที ปี
# "%H"(Capital H) = Hour
# "%M"(Capital M) = Minute
# "%S"(Capital S) = Second
# "%p" = เป็นการบอกว่าตอนนี้เป็น PM or AM
# "%j" = เป็นการถามว่าวันที่นั้นๆเป็น "วันที่เท่าไรของปี"
# "%a"(small a) = เป็นการถามว่าวันที่นั้นๆเป็น "วันอะไร" (แบบย่อ)
# "%A"(Capital A) เป็นการถามว่าวันที่นั้นๆเป็น "วันอะไร" (แบบเต็ม)
# "%w" = เป็นการถามว่าวันที่นั้นๆเป็น "ลำดับวันที่เท่าไรของสัปดาห์" # เริ่มนับตั้งแต่ 0 = sunday , 1 = monday ....
# "%b"(small b) = เป็นการถามว่าเดือนนั้นๆเป็น "เดือนอะไร" (แบบย่อ)
# "%B"(Capital b) = เป็นการถามว่าเดือนนั้นๆเป็น "เดือนอะไร" (แบบเต็ม)

import datetime

result=datetime.datetime.now() # ดึงวัน / เวลาปัจจุบันมาใช้งาน
# print(result.year) # เอาเฉพาะปีมาแสดง
# print(result.month) # เอาเฉพาะเดือนมาแสดง

newdate=datetime.datetime(2020,6,20,12) # yyyy,m,d
# print(newdate)

# รูปแบบแสดงผล
print("เริ่มต้น = ",result)
print(result.strftime("%x"))
print(result.strftime("%X"))
print(result.strftime("%c"))

# เวลา
print(result.strftime("%H"))
print(result.strftime("%M"))

# เขียนร่วมกัน
print(result.strftime("%H:%M:%S %p"))

# 1 - 365
print(result.strftime("%j"))

# Date
print(result.strftime("%a"))
print(result.strftime("%A"))
print(result.strftime("%w")) # 0 = sunday
print(result.strftime("%b"))
print(result.strftime("%B"))

print(result.strftime("%b วันที่ %a")) # วันที่ วัน เดือน