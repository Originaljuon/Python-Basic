import os
try:
    if os.path.exists("Score.txt"):
        os.remove("Score.txt")
        print("ลบแล้วนะครับ")
    else :
          print("ไม่พบไฟล์นี้ครับผม")
    # fr=open("Score.txt","r",encoding="utf-8")
    # line=fr.readlines()
    # for x in line: # ค่า x และ ค่า line "มีการจัดเก็บข้อมูลเป็น String" ฉะนั้นการระบุข้อมูลต้องอ้างอิงตามแบบ String
    #     print("=>",x)
        
	
    # fw=open("Score.txt","a",encoding="utf-8")
    # for i in range(2) :
    #     name=input("ป้อนข้อความที่ต้องการ : ")
    #     fw.writelines(name+"\n")
    # fw.close()
    # fr.close()
except FileNotFoundError :
    print("หาไฟล์ไม่เจอจ้า")
    
    """ 
    	การลบไฟล์ Text
		1. ต้องมีการเขียน import os เข้ามาทำงาน
        2. ป้อนคำสั่งว่า os.remove("ชื่อไฟล์ที่ต้องการจะลบ")
	"""