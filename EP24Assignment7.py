# Fahrenheit and Celsius

'''
สูตรการแปลงอุณหภูมิ
Celsius = (F - 32) x 5 / 9
Fahrenheit = (C x 9/5) + 32

'''

# แปลงอุณหภูมิ
temp = input("ป้อนอุณหภูมิ (องศา) :") #45C

degree= int(temp[:-1]) # โคล่อนเป็นการบอกว่าให้ข้อมูลทั้งหมดยกเว้นตัวที่กำหนด(ด้านหลังโคล่อน)
unit=temp[-1].upper() #แปลงค่าข้อมูลให้เป็นตัวพิมพ์ใหญ่แม้ผู้ป้อนข้อมูลจะป้อนพิมพ์เล็กเข้ามา


if unit=="C":
    result=(9*degree)/5+32
    unit_result="ฟาเรนไฮน์"
if unit=="F":
    result=(degree-32)*5/9
    unit_result="เซลเซียส"


print("แปลงตัวเลข = ",temp.upper()," เป็น ",unit_result," = ",result)