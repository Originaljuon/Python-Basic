# สร้างฟังก์ชั่นหาค่า Factorial

# หาค่า Factorial 5!

def factorial(number):
    if number==1:
        return number
    else :
        return number * factorial(number-1)


x=factorial(5)
print(x)


