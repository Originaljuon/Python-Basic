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

# try:
    # คำสั่งรันโปรแกรมปกติ
# except:
    # คำสั่งที่ทำงานตอนโปรแกรมมีข้อผิดพลาด
try:
    number1=int(input("ป้อนตัวเลข 1 :"))
    number2=int(input("ป้อนตัวเลช 2 :"))
    result=number1/number2
    print(result)
except:
    print("โปรแกรมมีข้อผิดพลาด")