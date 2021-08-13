a = 0
b = 1
for i in range(0, 48):
    c = a + b
    if c ** 0.5 % 1 == 0:
        print(str(c) + ' is a perfect square ')
    a = b
    b = c
