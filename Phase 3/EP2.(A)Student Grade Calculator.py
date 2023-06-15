# โปรแกรมคำนวณเกรดนักเรียน
try:
	# fw=open("Score.txt","a",encoding="utf-8")
	# while True:
	# 	studentid=input("ป้อนรหัสนักเรียน:")
	# 	if studentid == "exit":
	# 		break
	# 	score=input("ป้อนคะแนนสอบ:")
	# 	fw.writelines(studentid+"\t"+score+"\n") # \t = เว้นช่องว่าง 1 ช่อง
	# fw.close
	fr=open("Score.txt","r",encoding="utf-8")
	fw=open("Grade.txt","w",encoding="utf-8") # สังเกตว่าใช้ "w" เพราะถ้ามีการแก้คะแนนที่ ไฟล์.txt จะมีการรื้อใหม่ทั้งหมด กรณีนี้จะเห็นได้ว่า "w" ดีกว่า "a"
	grade=None
	for line in fr.readlines():
		score=line[-3:].strip() # รหัส คะแนน # ข้อสังเกต ถ้าเขียน index ว่า [-3:-1] คนที่ได้ 100 คะแนน จะถูกระบุแค่ 10 ที่ถูกควรเขียนว่า "[-3:]"
								# .strip = เป็นการบอกว่าให้ลบช่องว่างทั้งหมดทิ้งและมีการจัดข้อมูลใหม่ให้มีความเป็นระเบียบขึ้น !!! Very Good !!!
		studenid=line[:-3].strip()
		# print("รหัส = ",studenid," คะแนน = ",score)
		score=int(score) # สามารถแปลงค่าเป็น int ตรงบรรทัด 13 ได้เป็น score=int(line[-3:]) แบบนี้ก็ได้
		if score>=80:
			grade="A"
		elif score>=70 and score<80:
			grade="B"
		elif score>=50 and score<70:
			grade="C"
		else:
			grade="F"
		print("รหัส = ",studenid," คะแนน = ",score ," เกรดที่ได้ = ",grade)
		fw.writelines(studenid+"\t"+str(score)+"\t"+grade+"\n") # \t = เว้นวรรค 1 ช่อง \n = ขึ้นบรรทัดใหม่ # ต้องมีการแปลง score กลับมาเป็น str อีกหนึ่งรอบ
	fw.close()

except Exception as e:
	print(e)