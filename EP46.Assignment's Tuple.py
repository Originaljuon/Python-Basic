# นำค่าใน tuple => ตัวแปร
tup=(10,20,30)
a,b,c=tup
print(a)
print(b)
print(c)
d=a+c
print(d)


# สลับ tuple
x=(50,60)
y=(88,99)

print("Before y =>",x)
print("Before y =>",y)
x,y=y,x

print("After x =>",x)
print("After x =>",y)