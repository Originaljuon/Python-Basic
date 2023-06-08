# # # Exception = เหตุการณ์ที่ทำให้เกิดข้อผิดพลาดของโปรแกรม
# # # Phase 3 เป็นในเรื่องของการจัดการข้อผิดพลาดภาษา Python
# # # คิดว่าต้องรวบรวมข้อผิดพลาดแล้วบันทึกเก็บเอาไว้
# number1=int(input("ป้อนตัวเลข 1 :"))
# number2=int(input("ป้อนตัวเลช 2 :"))
# result=number1/number2
# print(result)
# # """
# # 1. SyntaxError = เกิดข้อผิดพลาดในการระบุไวยากรณ์ภาษา กรณีไม่ใช่ Exception
# # 2. ValueError
# # 3. ZeroDivisionError
# """

# try / except
# try:
    # คำสั่งรันโปรแกรมปกติ
# except:
    # คำสั่งที่ทำงานตอนโปรแกรมมีข้อผิดพลาด
try:
    # number1=int(input("ป้อนตัวเลข 1 :"))
    # number2=int(input("ป้อนตัวเลช 2 :"))
    # result=number1/number2
    # print(result)
	score=100+"50"
	print(score)
except Exception as e:  
	print (e)
	""" อันนี้ดีให้คอมบอกให้ว่าเกิดปัญหาอะไรไม่ต้องแยกระบุไปที่ละครั้ง """
else :
      print("จบโปรแกรม")
# except ValueError:
#     print("ต้องป้อนตัวเลขเท่านั้นถึงจะหารได้")
# except ZeroDivisionError:
#     print("ห้ามหารด้วยเลขศูนย์นะครับ")
# except TypeError:
#     print("ชนิดข้อมูลไม่ตรงกัน")