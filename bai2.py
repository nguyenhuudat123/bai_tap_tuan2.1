import math

x = float(input("nhập số thực x bất kì x= "))
y = float(input("nhập số thực y bất kì y= "))
z = float(input("nhập số thực z bất kì z= "))

f = (x + y + z) / (x*x + y*y + 1) - math.fabs(x - z * math.cos(y))
print(f"gia tri cua F la {f}")