import random

a = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
n = int(input("какая будет длина пароля: "))
p = ""

while n > 0:
    n -= 1
    p += a[random.randint(0,len(a)-1)]

print(p)
