# สร้างฟังก์ชั่นหาค่า Factorial
"""
factorial คือ การคูณเรียงตามลำดับลดหลั่นกันมา
ตัวอย่าง 5! = 5 x 4 x 3 x 2 x 1
"""
# หาค่า Factorial 5!

def factorial(number):
    if number==1:
        return number
    else :
        return number * factorial(number-1)


x=factorial(5)
print(x)


