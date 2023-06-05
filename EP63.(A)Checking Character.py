# หาจำนวนตัวอักษรพิมพ์เล็ก/พิมพ์ใหญ่
# upper = ตัวพิมพ์ใหญ่ , lower = ตัวพิมพ์เล็ก
def checkString(message):
	result={"UPPER":0,"LOWER":0} # ใช้ข้อมูลแบบ dictionary ในการแก้ปัญหา ต้องไปศึกษาเพิ่มเติมลืมหมดแล้ว
	for c in message:
		if c.isupper():
			result["UPPER"]+=1
		elif c.islower():
			result["LOWER"]+=1
		else:
			pass
	return result
