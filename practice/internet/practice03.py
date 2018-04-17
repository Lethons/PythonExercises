for i in range(10000):
    x = int((i + 100) ** 0.5)
    y = int((i + 268) ** 0.5)
    if (x * x == i +100) and (y * y == i + 268):
        print(i)

