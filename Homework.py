for i in range(0, 21):
    for j in range(0, int((100 - 5 * i) / 3) + 1):
        if 5 * i + 3 * j + (100 - i - j) / 3 == 100:
            print(str(i) + ' ' + str(j) + ' ' + str(100 - i - j))




