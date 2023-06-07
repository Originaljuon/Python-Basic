# Pass คือ กรณีเราสร้างชื่อฟังก์ชั่นมาแล้วแต่ยังไม่มีการดำเนินการภายในฟังก์ชั่นเราต้องการให้มันไม่ขึ้น Error

def getName():
    pass # แค่พิมพ์ว่า pass !! เสร็จแล้ว !! โปรแกรมก็จะ Run ผ่านไปก่อน
def getNamex(name):
    print("Hello , ",name)
def getNamexx(name): # เป็นไอเดียรูปแบบหนึ่งในการสรรค์สร้างโดยมี Pass เข้ามาในส่วนช่วยเจตนาเพื่อคัดกรองข้อมูล # ไม่ใช่เหมือนตอนแรกที่เจตนาเพราะยังคิดเนื้อหาภายในฟังก์ชั่นไม่ได้
    if name == "Kong":
        print("ยินดีด้วย")
    else :
        pass


getName()
getNamex("KongRuksiam")
getNamexx("Jojo")
getNamexx("Kong")