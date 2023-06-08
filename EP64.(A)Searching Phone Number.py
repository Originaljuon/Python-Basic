# ค้นหาเบอร์โทรศัพท์

data={"191":"แจ้งเหตุด่วน","1668":"รถโรงพยาบาล","1447":"ดับเพลิง"}

def searchNumber(message):
    for key , value in data.items():
        if value==message:
            print("เบอร์ติดต่อ = ",key)
        else :
            break
			# ยังมีปัญหาอยู่ว่าค่า else ต้องทำยังไงมันถึงจะ Smooth คือ ต้องการให้เป็นค่าว่างและมีการเช็ค key ต่อไปใน kongruksiam เหมือนจะไม่ถูกต้อง

message=input("ป้อนข้อมูลที่ต้องการ = ")
searchNumber(message)


