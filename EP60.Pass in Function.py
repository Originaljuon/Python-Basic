# Pass คือ กรณีเราสร้างชื่อฟังก์ชั่นมาแล้วแต่ยังไม่มีการดำเนินการภายในฟังก์ชั่นเราต้องการให้มันไม่ขึ้น Error

def getName():
    pass # แค่พิมพ์ว่า pass !! เสร็จแล้ว !! โปรแกรมก็จะ Run ผ่านไปก่อน
def getNamex(name):
    print("Hello , ",name)
def getNamexx(name):
    if name == "Kong":
        print("ยินดีด้วย")
    else :
        pass


getNamexx("Jojo")
getNamexx("Kong")
getName()
getNamex("KongRuksiam")