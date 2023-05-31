# non primitive : list
# number=[] #list ว่าง
# number=[1,2,3,4,5,6] # list มีสมาชิก 1-6
# name=["นาย A","นาย B","นาย C"] #list name มีสามชิก
# all=[10,"นายไข่",True,3.14,-10]
# #constructor
# name=list(["นาย A","นาย B","นาย C"])

# #เข้าถึงข้อมูลของ List
# print(all[-3:])

number=[1,2,3,4,5,6,7,8,9,10]
fruit=["มะม่วง","มะนาว","มะยม","มะละกอ"]

# # การแก้ไขข้อมูล
# # ชื่อตัวแปร [index] = "ข้อมูลที่แก้ไข"

# print("ก่อนแก้ไข => " ,number)

# number[2]=9
# number[-1]=10
# print("หลังแก้ไข => ",number)

# sum=0
# for x in number:
# 	sum+=x #sum=sum+x
# print(sum)

# print(len(number))
# print(len(fruit))

print("หลังเพิ่ม=>",fruit)
fruit.insert(1,"ทุเรียน")
print("หลังแทรก=",fruit)

fruit.remove("มะยม")
print(fruit)