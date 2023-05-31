tup=100,99,88,50,200,1,2,3,4,3.99,4 # tuple

# # lis=list([1,2,3,4,"kongruksiam","มะม่วง",True,3.99]) # list

# # lis[0]="กรุงเทพ" # หมายถึงให้คำว่ากรุงเทพแทนค่าคำที่อยู่ตำแหน่งแรกของ list นั่นก็คือ 1
# # print(tup)
# # print(tup[:-1])
# print("ก่อนแก้ไข => ",tup)
# # แปลงข้อมูล
# lis=list(tup)
# lis[0]="กรุงเทพ"

# tup=tuple(lis)
# # print("หลังแก้ไข => ",tup)

# print(len(tup))

# for item in range(len(tup)):
# #     print(tup[item])

# name=("kongruksiam","jojo")
# new=("nut","nack")

# name=name+new # ถ้าต้องการลดรูปจะเขียได้เป็น name+=new
# print(name)

# lis=list(tup)
# city=["กรุงเทพ","ชลบุรี","อุบล"]
# tup=tup+tuple(city)
# print("Before =>",tup)
# lis=list(tup)
# lis.remove("มะม่วง")
# tup=tuple(lis)
# print(lis)

# x=tup.index(4)
# print(x)
print("Before=>",tup)
lis=list(tup)
lis.sort()
lis.reverse()
tup=tuple(lis)
print("After=>",tup)